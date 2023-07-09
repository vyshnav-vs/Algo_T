from kite_trade import *
import time
import threading
import random
import pandas as pd
import datetime




enctoken = "1hyjvxh/60RYtgGFjblX1QiA3dV2cNIc6lIpfaND7bWUdzXC7S759SbqVwFCuK3tZKQUigo8DxrZiHE7Xy9Aui7C+5hi5VbTKQHJzWQxGXwyevaoQ2CfyQ=="
kite = KiteApp(enctoken=enctoken)
#print(kite.ltp(["NSE:NIFTY 50", "NSE:NIFTY BANK"]))

def trade(name,kite):
    name1="NSE:"+name
    target_time=datetime.time(9,15)
    ltp=[]
    buy=0
    while True:
        # Get the latest LTP from the broker's API
        wanted=kite.ohlc(name1)[name1]
        print(wanted['ohlc']['open']*(1+0.01))
        if len(ltp)<3:
            ltp.append(wanted['last_price'])
            time.sleep(60) 
            continue
        ltp.append(wanted['last_price'])
 
        # Append the latest LTP to the list
        
        qty=1
        if((ltp[-1]>(2*wanted['ohlc']['low']+wanted['ohlc']['open'])/3) and (ltp[-2]>(2*wanted['ohlc']['low']+wanted['ohlc']['open'])/3)and (ltp[-3]<(2*wanted['ohlc']['low']+wanted['ohlc']['open'])/3) and buy==0  and kite.margins()['equity']['net'] *5 > ltp[-1]) :
            buy=1
            print(wanted['ohlc']['open'])
            qty=1
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
        if((ltp[-1]<(2*wanted['ohlc']['high']+wanted['ohlc']['open'])/3) and (ltp[-2]<(2*wanted['ohlc']['high']+wanted['ohlc']['open'])/3)and (ltp[-3]>(2*wanted['ohlc']['high']+wanted['ohlc']['open'])/3) and buy==1  and kite.margins()['equity']['net'] *5 > ltp[-1]) :
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



        time.sleep(60) 



        
        
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
    

