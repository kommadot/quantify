import pandas as pd
import numpy as np

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "backend.settings") 
import django 
django.setup()

from api.models import StockPrice
from django.forms.models import model_to_dict

from datetime import datetime
from datetime import timedelta

from threading import Thread

class LV:
    def __init__(self):
        self.df = pd.DataFrame(columns=['종목', '변동성'])
        self.cnt = 0
        self.SP = StockPrice.objects.all()
    def getLV(self, start, end, test_date):
        end = end if end <= self.SP.count() else self.SP.count()
        SP = self.SP[start:end]
        df = pd.DataFrame(columns=['종목', '변동성'])
        # test_date = datetime.strptime(test_date, "%Y-%m-%d")
        for i in range(end-start):
            print(self.cnt)
            stock = model_to_dict(SP[i])
            stock_code = stock['code']
            stock_price = pd.DataFrame(stock['data'])
            t = timedelta(days=365)
            # df.dropna()를 이용해 결측값 있는 행 제거
            stock_price = stock_price.dropna()
            # 데이터의 타입을 int형으로 바꿔줌
            stock_price[['open', 'high', 'low', 'close', 'volume']] = stock_price[['open', 'high', 'low', 'close', 'volume']].astype(int)
            # 컬럼명 'time'의 타입을 date로 바꿔줌
            stock_price['time'] = pd.to_datetime(stock_price['time'])
            stock_price = stock_price[(stock_price.time>=test_date-t) & (stock_price.time<=test_date)]
            price_close = stock_price['close']
            price_profit = price_close.pct_change()
            # 변동성
            price_variability = price_profit.std() * np.sqrt(len(stock_price))
            df.loc[i, ['종목']] = stock_code
            df.loc[i, ['변동성']] = price_variability
            # print(i)
            self.cnt+=1
        # print(self.df)
        self.df = self.df.append(df)
        return self.df
    
    def run(self,test_date):
        self.thread_init(test_date)
        self.thread_run()

        return self.df
        
    def thread_init(self,test_date):
        START, END = 0, 0
        self.threads = []
        ma = self.SP.count()
        ma = 100
        qu = ma//4
        END = START + qu
        for i in range(4):
            self.threads.append(Thread(target=self.getLV, args=(START, END, test_date)))
            START += qu
            END += qu
        self.thread_run()
        
    def thread_run(self):
        for i in self.threads:
            i.start()
        for i in self.threads:
            i.join()
        self.df = self.df.sort_values(by=["변동성"], ascending=True)


# a = LV()
# a.thread_init("2020-08-20")
# print(a.df)