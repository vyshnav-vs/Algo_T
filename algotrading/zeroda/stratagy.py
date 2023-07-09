import time
import random

# Assuming you can get the LTP from your broker's API or any other method

# Define the moving average window sizes
sma_13_window = 13
sma_48_window = 48

# Initialize the lists to store LTP and moving averages
ltp_list = []
sma_13_list = []
sma_48_list = []

while True:
    # Get the latest LTP from the broker's API
    ltp = get_latest_ltp()  # Replace with your method to get the LTP
    
    # Append the latest LTP to the list
    ltp_list.append(ltp)
    
    # Calculate the moving averages
    sma_13 = sum(ltp_list[-sma_13_window:]) / sma_13_window if len(ltp_list) >= sma_13_window else None
    sma_48 = sum(ltp_list[-sma_48_window:]) / sma_48_window if len(ltp_list) >= sma_48_window else None
    
    # Append the moving averages to their respective lists
    sma_13_list.append(sma_13)
    sma_48_list.append(sma_48)
    
    # Check for a moving average crossover
    if sma_13 is not None and sma_48 is not None:
        if sma_13 > sma_48:
            # Place a buy order
            print("Buy signal")
        elif sma_13 < sma_48:
            # Place a sell order
            print("Sell signal")
    
    # Delay for some time before retrieving the next LTP
    time.sleep(60)  # Delay for 1 minute (adjust as per your requirements)
