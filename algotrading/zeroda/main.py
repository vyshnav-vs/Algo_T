from kite_trade import *
import time
import threading
import random
import pandas as pd

enctoken = "rBe/6uGyeWBzsnYsUsNPCZktdlsQWI3wr/6DLfLahUbwu64ZY5QH/AGpqGK4sO9QU1L/SVAR2DUDg2ZI9nHKFmGnfEuDrD3dJihxNRLCuTIs8Y9EfsR+dw=="
kite = KiteApp(enctoken=enctoken)
#print(kite.ltp(["NSE:NIFTY 50", "NSE:NIFTY BANK"]))
def trade(name,kite):
    try :
        name=name.upper()
        name1="NSE:"+name
        sma_13_window = 13
        sma_48_window = 48

        # Initialize the lists to store LTP and moving averages
        ltp_list = []
        sma_13_list = []
        sma_48_list = []

        while True:
            # Get the latest LTP from the broker's API
            ltp = kite.ltp(name1)[name1]["last_price"]  # Replace with your method to get the LTP
            
            # Append the latest LTP to the list
            ltp_list.append(ltp)
            
            # Calculate the moving averages
            sma_13 = sum(ltp_list[-sma_13_window:]) / sma_13_window if len(ltp_list) >= sma_13_window else None
            sma_48 = sum(ltp_list[-sma_48_window:]) / sma_48_window if len(ltp_list) >= sma_48_window else None
            
            # Append the moving averages to their respective lists
            sma_13_list.append(sma_13)
            sma_48_list.append(sma_48)
            buy=0
            # Check for a moving average crossover
            if sma_13 is not None and sma_48 is not None:
                if sma_13 > sma_48 and not buy:
                    # Place a buy order
                    if kite.margins['equity']['net'] *5 > ltp:
                        order = kite.place_order(variety=kite.VARIETY_REGULAR,
                            exchange=kite.EXCHANGE_NSE,
                            tradingsymbol=name,
                            transaction_type=kite.TRANSACTION_TYPE_BUY,
                            quantity=int(kite.margins['equity']['net'] *5 / ltp),
                            product=kite.PRODUCT_MIS,
                            order_type=kite.ORDER_TYPE_MARKET,
                            price=None,
                            validity=None,
                            disclosed_quantity=None,
                            trigger_price=None,
                            squareoff=None,
                            stoploss=None,
                            trailing_stoploss=None,
                            tag="TradeViaPython")
                        buy=ltp
                    print("Buy signal")
                elif sma_13 < sma_48 and buy:
                    order = kite.place_order(variety=kite.VARIETY_REGULAR,
                            exchange=kite.EXCHANGE_NSE,
                            tradingsymbol=name,
                            transaction_type=kite.TRANSACTION_TYPE_SELL,
                            quantity=int(kite.margins()['equity']['net'] *5 / buy),
                            product=kite.PRODUCT_MIS,
                            order_type=kite.ORDER_TYPE_MARKET,
                            price=None,
                            validity=None,
                            disclosed_quantity=None,
                            trigger_price=None,
                            squareoff=None,
                            stoploss=None,
                            trailing_stoploss=None,
                            tag="TradeViaPython")
                    buy=0
                    # Place a sell order
                    print("Sell signal")
            
            # Delay for some time before retrieving the next LTP
            time.sleep(60)  # Delay for 1 minute (adjust as per your requirements)
    except:
        print(name)


        
        
    #fil.write("Trade done\n")
    
d=[]#li1mit to 10 stocks
thds=[]
df=pd.read_csv('this.csv')
while (1):

    print("Welcome ")
    tra=input("enter the trading symbol")

    x = threading.Thread(target=trade, args=(tra,kite,))
    thds.append(x)
    x.start()
    

