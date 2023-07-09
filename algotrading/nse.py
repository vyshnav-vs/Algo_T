import requests , pandas as pd
from io import BytesIO

class NSE():
    def __init__(self, timeout=10)-> None:
        self.base_url="http://www.nseindia.com"
        self.headers={'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0'}
        self.timeout=timeout
        self.cookies=[]
    
    def __getCookies(self,renew=False):
        if len(self.cookies)>0 and renew == False:
            return self.cookies
        
        r=requests.get(self.base_url,timeout=self.timeout,headers=self.headers)
        self.cookies=dict(r.cookies)
        return self.__getCookies()
    
    def getHistoricalData(self,symbol,series,form_date, to_date):
        
        url="/api/historical/cm/equity?symbol={0}&series=[%22{1}%22]&from={2}&to={3}&csv=true".format(symbol.replace("&","%26"),series,form_date.strftime("%d-%m-%y"),to_date.strftime("%d-%m-%y"))
        response=requests.get(self.base_url+url,headers=self.headers,timeout=self.timeout,)

        df=pd.read_csv(BytesIO(response.content),sep=',',thousands=',')
        df=df.rename(columns={"Date ":'date','series ':'series','OPEN ':'open','HIGH ':'high','LOW ':'low',
                                'PREV. CLOSE':'prev_close','ltp ':'ltp','close ':'close','52W H ':'hi_52_wk','52W L ':'lo_52_wk',
                                'VOLUME ':'volume','VALUE ':'value',"No of trades ":'trades'})
        
        




if __name__=="__main__":
    from datetime import date
    from nse import NSE
    api=NSE()
    df=api.getHistoricalData("SBIN",'EQ',date(2023,1,1),date(2023,6,21))
    print(df)