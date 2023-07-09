from kite_trade import *
import time
import threading
import pandas as pd

enctoken = "1hyjvxh/60RYtgGFjblX1QiA3dV2cNIc6lIpfaND7bWUdzXC7S759SbqVwFCuK3tZKQUigo8DxrZiHE7Xy9Aui7C+5hi5VbTKQHJzWQxGXwyevaoQ2CfyQ=="
kite = KiteApp(enctoken=enctoken)
print(kite.margins()['equity']['net'])
df=kite.ohlc("NSE:VBL")['NSE:VBL']['ohlc']['open']
print(df)