from kite_trade import *
import time
import threading
import random
import pandas as pd
import datetime

#GLobal Variables
enctoken = "WshusteA1Ze+IcwXxkd9WDBQsnGRE/xgbrgVhopiD1nBray5PmD7GgEP1tlyuQKf30M1g0ZHL+vU6/AOZMRS8j1DoDrX30d/nFoRpQiWP6nUWxSYaLyaaQ=="
kite = KiteApp(enctoken=enctoken)
max_trade_margin = 10000


#print(kite.ltp(["NSE:NIFTY 50", "NSE:NIFTY BANK"]))
def quatitty(price):
    '''
    Function that calculates the total Quantity to be traded

    arg:
        price: price at which the trade has to be done.

    returns:
        The net quatity of asset to be traded.
    '''

    acc_balance = kite.margins()
    if acc_balance > max_trade_margin:
        return max_trade_margin//price
    else:
        return acc_balance//price
    
    
def is_market_open():
    '''
    Function that checks whether market is open or not.

    '''
    now = datetime.datetime.now().time()
    market_open = datetime.time(9, 15)  # Market opening time
    market_close = datetime.time(15, 30)  # Market closing time

    # Check if the current time is within market hours
    return market_open <= now <= market_close


def trade(symbol, kite, targets, entry):
    '''
    Function that executes an intraday trade as type market order. 

    arg:
        symbol : Asset trading symbol
        kite : Kite app API object
        targets : Target price
        entry : Entry price 

    '''
    ticker="NSE:"+ symbol
    target_time=datetime.time(9,15)
    print("ivide")
    while (not is_market_open()):
        print("evide")
        time.sleep(60)
    try:
        print(kite.ohlc(symbol)[ticker])
    except:
        return

    buy=0
    while True:
        # Get the latest LTP from the broker's API
        wanted=kite.ohlc(ticker)[symbol]
        qty=0

        if (wanted['last_price'] == entry and buy == 0) :
            buy=1
            print(wanted['ohlc']['open'])
            qty= quatitty(entry)
            print(qty)
            if qty:
                order = kite.place_order(variety=kite.VARIETY_REGULAR,
                                exchange=kite.EXCHANGE_NSE,
                                tradingsymbol=symbol,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=qty,
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
        if(wanted['last_price'] == targets and buy == 1) :
            buy=0
            order = kite.place_order(variety=kite.VARIETY_REGULAR,
                            exchange=kite.EXCHANGE_NSE,
                            tradingsymbol=symbol,
                            transaction_type=kite.TRANSACTION_TYPE_SELL,
                            quantity=qty,
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
            break



        time.sleep(5) 



        
        
    #fil.write("Trade done\n")
    
d=[] #limit to 10 stocks
thds=[]
df = pd.read_csv('this.csv')
while (1):
    print("Welcome ")
    symbol = input("enter the trading symbol")
    entry = int(input("Enter input price"))
    target = int(input("Enter target"))

    x = threading.Thread(target=trade, args=(symbol,kite,target,entry,))
    thds.append(x)
    x.start()
    

