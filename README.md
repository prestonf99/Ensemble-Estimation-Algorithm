# Ensemble Estimation Algorithm - Test Run 
by Preston Fisk

April 18, 2024


## Features

This package trains an ensemble estimation algorithm then deploys it into real-time trading using the Oanda API for the testing. The model is trained to make binary predictions regarding the future price action of an underlying asset (in our case EUR_USD), by taking the asset's price, the asset's returns, and the asset's lagged returns (lagged by 3). If the model thinks that the next return will be positive, it puts out +1. If negative, -1. We then implement it using a class called `EnsembleTrader.py` that utilizes an Oanda API wrapper package, tpqoa (https://github.com/yhilpisch/tpqoa). It takes incoming price data, resamples the data, calculates the last price for the interval provided (in our case, 5-minute bars), implements lags, and then applies our ensemble estimation algorithm to generate predictions in real-time. Included in the on_success is the trading logic that we'll implement as well. After the running the algorithm in real-time, the Jupyter Notebook file `Algorithm_Implementation.ipynb` has a section that allows the user to review the algorithm's performance visually. 

## Installation
To set up the environment:
1. Install the required Python packages:
    
        pip install numpy pandas sklearn matplotlib 

2. Install tpqoa Oanda API package:

    https://github.com/yhilpisch/tpqoa
    
    Go to the README for detailed instructions. We personally prefer using a cloud service (DigitalOcean) inside of a docker container when using the Oanda API.
    
3. Setup an 'oanda.cfg' file:

*The format is as follows* 
    
        [oanda]
        account_id = [YOUR_ACCOUNT_ID]
        access_token = [YOUR_ACCESS_TOKEN]
        account_type = practice

## Usage

1. Retrieve historical data from the Oanda API.
2. Train the AdaBoostRegressor model with the historical data (or a model of your choice!)
3. Implement the 'EnsembleTrader' class that handles the trading logic & live implementation:

        import warnings 
        warnings.simplefilter('ignore')
        Import EnsembleTrader as ES
        
        es = ES.EnsembleTrader('oanda.cfg',
                                instrument=your_instrument,
                                bar_length = '5T',
                                ensemble = your_model,
                                units = your_unit_size,
                                stop = None, #Runs until manually stopped
                                lags = 3) #Designed to run 3.
        
        es.begin_trading(instrument, stop=None)
        
4. Review your model's performance.

    You will need to fill in the 'tid' to match the 'tid' of the first trade in your live session in the cell above.
