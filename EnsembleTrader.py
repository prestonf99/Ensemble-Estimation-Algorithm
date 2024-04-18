import tpqoa
import numpy as np
import pandas as pd
from datetime import datetime
api = tpqoa.tpqoa('oanda.cfg')

class EnsembleTrader(tpqoa.tpqoa):
    def __init__(self, conf_file, instrument, bar_length, ensemble, units, stop,
                 lags, *args, **kwargs):
        super(EnsembleTrader, self).__init__(conf_file)
        self.position = 0
        self.instrument = instrument
        self.ensemble = ensemble
        self.bar_length = bar_length
        self.lags = lags
        self.units = units
        self.stop = stop
        self.tick_data = pd.DataFrame()
        self.cols = []
        self.min_length = self.lags + 2
        self.initialized = False

    def on_success(self, time, bid, ask):
        # Since i dont want it to stream the number of ticks,
        # I created a notification of when it goes live.
        if not self.initialized:
            print(f'Trading algorithm is running as of {datetime.now()}')
            self.initialized = True
        #New Dataframe Setup
        new_row = (pd.DataFrame({'bid':bid, 'ask':ask}, index=[pd.Timestamp(time)]))
        self.tick_data = pd.concat([self.tick_data, new_row])
        self.data = self.tick_data.resample(
            self.bar_length, label='right').last().ffill().iloc[:-1]
        #Calculating Market Price & Returns
        self.data['price'] = self.data.mean(axis=1)
        self.data['returns'] = np.log(self.data['price'] /
                                      self.data['price'].shift(1))
        #Implementing lags, as the model was fitted with lags
        self.cols = []
        for lag in range(1, self.lags + 1):
            col = f'lag_{lag}'
            self.data[col] = self.data['returns'].shift(lag)
            self.cols.append(col)
        self.tick_data.to_csv('tick_output.csv')
        self.data.dropna(inplace=True)
        
        # Ensuring the model isn't trying to predict on an empty data set.
        if not self.data.empty:
            self.data['ensemble_prediction'] = self.ensemble.predict(self.data[self.cols])
            self.data['prediction'] = np.where(self.data['ensemble_prediction'] >
                                               0, 1, -1)
    


            # Implementing the trading logic. 
            if len(self.tick_data) > self.min_length:
                self.min_length += 1
                # If the previous prediction was 1
                if self.data['prediction'].iloc[-1] == 1:
                    #Long if there is no Position.
                    if self.position == 0:
                        self.create_order(self.instrument, self.units)
                    # If short, buy twice as many units
                    elif self.position == -1:
                        self.create_order(self.instrument, self.units * 2)
                    # Otherwise, leave the position
                    self.position = 1
                elif self.data['prediction'].iloc[-1] == -1:
                    if self.position == 0:
                        self.create_order(self.instrument, -self.units)
                    elif self.position == 1:
                        self.create_order(self.instrument, -self.units * 2)
                    self.position = -1
        
    # Closing out an open position.
    def close_position(self):
        if self.position > 0:
            units_to_close = -self.units
            self.create_order(self.instrument, units_to_close)
        elif self.position < 0:
            units_to_close = self.units * -1
            self.create_order(self.instrument, units_to_close)
            
    def begin_trading(self, instrument, stop):
        try:
            self.stream_data(instrument, stop=stop)
        except KeyboardInterrupt:
            print('Trading stopped by user -- Flattening Positions')
            self.close_position()
