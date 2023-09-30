from kite_trade import *
import time
import threading
import random
import pandas as pd
import datetime




enctoken = "WshusteA1Ze+IcwXxkd9WDBQsnGRE/xgbrgVhopiD1nBray5PmD7GgEP1tlyuQKf30M1g0ZHL+vU6/AOZMRS8j1DoDrX30d/nFoRpQiWP6nUWxSYaLyaaQ=="
kite = KiteApp(enctoken=enctoken)
#print(kite.ltp(["NSE:NIFTY 50", "NSE:NIFTY BANK"]))
def quatitty(price):
    remaining=kite.margins()
    if remaining>10000:
        return 10000//price
    else:
        return remaining//price
def is_market_open():
    now = datetime.datetime.now().time()
    market_open = datetime.time(9, 15)  # Market opening time
    market_close = datetime.time(15, 30)  # Market closing time

    # Check if the current time is within market hours
    return market_open <= now <= market_close
def trade (name,kite,targets, entry):
    name1="NSE:"+name
    target_time=datetime.time(9,15)
    print("ivide")
    while (not is_market_open()):
        print("evide")
        time.sleep(60)
    try:
        print(kite.ohlc(name)[name1])
    except:
        return

    buy=0
    while True:
        # Get the latest LTP from the broker's API
        wanted=kite.ohlc(name1)[name1]
        qty=0

        if(wanted['last_price'] == entry and buy ==0) :
            buy=1
            print(wanted['ohlc']['open'])
            qty= quatitty(entry)
            print(qty)
            if qty:
                order = kite.place_order(variety=kite.VARIETY_REGULAR,
                                exchange=kite.EXCHANGE_NSE,
                                tradingsymbol=name,
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
                            tradingsymbol=name,
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
    
d=[]#li1mit to 10 stocks
thds=[]
df=pd.read_csv('this.csv')
while (1):
    print("Welcome ")
    tra=input("enter the trading symbol")
    entry=int(input("Enter input price"))
    target=int(input("Enter target"))

    x = threading.Thread(target=trade, args=(tra,kite,target,entry,))
    thds.append(x)
    x.start()
    

