## Practice Project Report -- Python For Algorithmic Trading

Preston Fisk

April 18, 2024

## Current Understanding of the Central Topics and Tools

This week was probably the most involved week I've had with the algorithmic trading topics covered in the course material to date. It was a challenging, yet enjoyable week. Currently, I'm relatively comfortable with Pandas, Matplotlib, and NumPy. I haven't used the Oanda API all that much because for my personal projects I tend to upload data from either yFinance or off of SierraChart's platform. It was great getting to use some real-time data and get comfortable with building a model that operated in real-time versus the things I generally do on my own time like Volatility Risk Premium calculations, how often particular intraday price moves occur, following day's returns based on the closing action, and so on. 

## Strengths and weaknesses discovered this week

There were a few things that definitely need work moving forward. First, I need to spend some more time with the ML packages (sklearn, tensorflow, etc). Moving forward, I intend on spending some more time in the AI in Finance lectures and material. One of my strengths is that I am extremely comfortable working with DataFrames to organize my data in a fashion that's useful for my purposes, which is great! Another strength is utilizing Matplotlib to visualize my data. This week was the first time I've ever used a GitHub repository, so I definitely need to spend some more time getting comfortable uploading my work to the world via GitHub. Another strength is utilizing docker containers and setting up python environments, I can setup a docker container with conda, screen, vim, and the relevant packages with little to no use of my notes. 

## My experiences doing it on my own

The code provided in the lectures is a fantastic resource. It's extremely useful to be able to look through the past lectures and the books to help sharpen your understanding in real time. One thing I really enjoyed and want to continue working on is creating position logic, it was definitely a highlight of the week and there's so many possibilities regarding how you can execute your orders and manage your risk. It was frustrating at times, but once the code begins working it's extremely satisfying. I had a lot of trouble setting up the live data in a fashion that allowed the model to utilize it, but it was all worth it once the model began working. It was fun getting to implement little tweaks that I thought made sense, for example:

Instead of streaming the data on the shell tick-by-tick and cluttering up the notebook:
        
        print(self.ticks, end=' ')

I implemented:

        if not self.initialized:
            print(f'Trading algorithm is running as of {datetime.now()}')

In my opinion, this was a much better solution that made running the model much less cluttered. 

## Opportunities to improve the existing materials and resources 

I know that there's some emphasis on 'choose one or two areas and stick with it', but it's probably wise to make it extremely clear. I've done a majority of the lectures across the Asset Management, Algorithmic Trading, Listed Volatility and Variance Deriviatives, Dx Analytics, and Computational Finance modules. Looking back on it, I wish I spent a majority of my time exclusively in the Algorithmic Trading Module to deepen my understanding. 

## Other Comments

Love the program, will be utilizing the wealth of material for years!