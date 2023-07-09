import time
import numpy as np
from kite_trade import *
import time
import threading

enctoken = "r99NJho+soHcCf26X7/G461dyB/rR6Qqi9ySzk5dxPFS6j85IzCcHZXBKd+H5Dm52DQaD2it6m6bN4gDFq0Ey2Je4vs0ofsXgXZIj1H1mYpgD/E56CZFOA=="
kite=KiteApp(enctoken)


symbol = 'BTC/USDT'  # Replace with the symbol you want to trade

# Set up the moving average lengths
short_ma_length = 13
long_ma_length = 48

# Function to calculate moving average
def calculate_ma(data, length):
    if len(data) < length:
        return None
    else:
        return sum(data[-length:]) / length

# Function to place a buy order
def place_buy_order(quantity):
    order = exchange.create_market_buy_order(symbol, quantity)

# Function to place a sell order
def place_sell_order(quantity):
    order = exchange.create_market_sell_order(symbol, quantity)

    while True:
        # Fetch recent price data
        candles = exchange.fetch_ohlcv(symbol, timeframe='1m', limit=50)  # Fetch 50 1-minute candles
        closes = [candle[4] for candle in candles]  # Extract closing prices

        # Calculate moving averages
        short_ma = calculate_ma(closes, short_ma_length)
        long_ma = calculate_ma(closes, long_ma_length)

        if short_ma is not None and long_ma is not None:
            # Check for crossover
            if short_ma > long_ma:
                # Place a buy order
                place_buy_order(0.001)  # Replace with your desired buy quantity

            elif short_ma < long_ma:
                # Place a sell order
                place_sell_order(0.001)  # Replace with your desired sell quantity

        time.sleep(60)  # Wait for 1 minute before checking again

while(True):
    time.sleep(1)
    print("Welcome ")
    d.append(input("Enter the stock you wish to interaday acc to the symbol provided in data 1"))
    nos=int(input("Enter nos"))
    
    x = threading.Thread(target=trade, args=(d[-1],nos,kite,))
    thds.append(x)
    x.start()