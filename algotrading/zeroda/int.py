from kite_trade import *
import time
import threading
import pandas as pd

enctoken = "Kv+fGcdvYi0P2trVPBGS0kl+8LhEdQNZvcxkK5aH0VsDJ+/Uriwju1qhTr5d/NYjL/KtaMLrP7PGPui8tozV1CjATx6r2Gon/gVWhXhJe0nqa0iOTWEa9w=="
kite = KiteApp(enctoken=enctoken)
data=pd.DataFrame(kite.instruments(exchange=kite.EXCHANGE_NSE))
df = pd.read_csv("MW-NIFTY-50-03-Jul-2023.csv")
symbol_list=df['SYMBOL\n']
df=pd.DataFrame(kite.instruments(exchange=kite.EXCHANGE_NSE))
df=df[df["tradingsymbol"].isin(symbol_list)].reset_index(drop=True)
df=df[['instrument_token','tradingsymbol','segment']]
df.to_csv()
print(df)