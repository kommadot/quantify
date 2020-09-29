import pandas as pd
import numpy as np
import datetime
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "backend.settings") 
import django 
django.setup()
from api.models import StockPrice
class Backtest:
    def __init__(self,start,end,strategy,budget, rebalance=6):
        self.start = datetime.datetime.strptime(start,'%Y-%m-%d')
        self.end = datetime.datetime.strptime(end,'%Y-%m-%d')
        self.current = start
        self.strategy = strategy
        self.budget = budget
        self.rebalance = rebalance
        self.df = pd.DataFrame(columns=['date','budget'])
        self.stock_list = [{'code':'005930'}]
    def run(self):
        day = datetime.timedelta(days=1)
        delta = datetime.timedelta(days=self.rebalance*30)
        date = self.start
        #리밸런싱 기간 안에서
        day_dic = {}
        cnt = 0
        while True: 
            #전략으로 테이블 받고
            #테이블의 종가들 검색해서 구매
            self.buy_stock()
            # df_marks = df_marks.append(new_row, ignore_index=True)
            day_date = date
            while day_date <= day_date+delta:
                self.df = self.df.append({'date':day_date,'budget':self.get_budget(day_date)})
                # self.df.loc[cnt]={'date':day_date,'budget':self.get_budget(day_date)}
                day_date+=day
                cnt+=1
            #리밸런싱 기간 루프
                #리밸런싱 기간동안 돌면서 데이타프래임에 현재 예산 넣고
            #다 판매
            self.sell_stock()
            if date < self.end:
                date = date+delta if date+delta<=self.end else self.end
                continue
            break
        #반환
        return self.df
        
    def buy_stock(self):
        pass
    def sell_stock(self):
        pass
    def get_budget(self,day):
        stock_sum = 0
        for row in self.stock_list:
            stock = StockPrice.objects.filter(code=row['code'])
            print(stock.count())
            df = pd.DataFrame(stock.data)
            print(df.loc[df['time'] == datetime.datetime.strftime('%Y-%m-%d')])
        return self.budget+stock_sum
a = Backtest("2020-01-20","2020-02-20",1,200000,3)
a.run()