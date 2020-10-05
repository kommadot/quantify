import pandas as pd
import numpy as np
import datetime
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "backend.settings") 
import django 
django.setup()
from api.models import StockPrice
import time
from django.forms.models import model_to_dict
# from .LowVariabilityClass import LV
class Backtest():
    def __init__(self,start,end,strategy,budget, rebalance=6):
        self.start = datetime.datetime.strptime(start,'%Y-%m-%d')
        self.end = datetime.datetime.strptime(end,'%Y-%m-%d')
        self.current = start
        self.strategy = strategy
        self.budget = budget
        self.start_budget = budget
        self.rebalance = rebalance
        self.df = pd.DataFrame(columns=['date','budget'])
        self.stock_list = []
        self.lv = LV()
        self.divide = 5
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

            self.buy_stock(date)
            # df_marks = df_marks.append(new_row, ignore_index=True)
            # day_date = date
            end = date + delta if date + delta <= self.end else self.end
            print(self.stock_list)
            while date < end:
                cur_budget = self.get_budget(date)
                if cur_budget == self.budget:
                    if date == self.start:
                        cur_budget = self.start_budget
                    else:
                        cur_budget = self.df[self.df['date']==(date-datetime.timedelta(days=1)).strftime("%Y-%m-%d")]['budget'].values[0]
                cur_budget = int(cur_budget)
                self.df = self.df.append({'date':date,'budget':cur_budget},ignore_index=True)
                print(date)
                date+=day
                cnt+=1
            
            #리밸런싱 기간 루프
                #리밸런싱 기간동안 돌면서 데이타프래임에 현재 예산 넣고
            #다 판매
            
            self.sell_stock(date)

            if date < self.end:

                # date = date+delta if date+delta<self.end else self.end
                continue
            break
        #반환
        return self.df
        
    def buy_stock(self,date):

        table = self.lv.run(date)
        budget_divide = self.budget/self.divide
        print(table)
        for i in range(self.divide):
            code = table.iloc[i].code
            
            print(code)
            stock = StockPrice.objects.get(code=code)
            stock = model_to_dict(stock)
            df = pd.DataFrame(stock['data'])
            cur_date = date
            price = 0
            while price==0:
                temp = df.loc[df['time'] == cur_date.strftime('%Y-%m-%d')]['close'].mean()
                if np.isnan(temp):
                    price=0
                else:
                    price=temp
                print(price)

                cur_date -= datetime.timedelta(days=1)
            print(price)
            quantity = budget_divide//price
            self.stock_list.append({"code":code,"quantity":quantity,"price":price})
            self.budget -= price*quantity

    def sell_stock(self,date):
        print("sell_start")
        for i in self.stock_list:
            stock = StockPrice.objects.get(code=i['code'])
            stock = model_to_dict(stock)
            df = pd.DataFrame(stock['data'])
            cur_date = date
            price = 0
            while price ==0 :
                temp = df.loc[df['time'] == cur_date.strftime('%Y-%m-%d')]['close'].mean()
                if np.isnan(temp):
                    price=0
                else:
                    price=temp
                print(price)
                cur_date -= datetime.timedelta(days=1)
            self.budget += i['quantity'] * price
        self.stock_list=[]

    def get_budget(self,day):
        stock_sum = 0
        for row in self.stock_list:
            stock = StockPrice.objects.get(code=row['code'])
            stock = model_to_dict(stock)
            df = pd.DataFrame(stock['data'])
            r = df.loc[df['time'] == day.strftime('%Y-%m-%d')]
            if len(r)==0:
                continue
            stock_sum += r['close'].values[0]*row['quantity']
        return self.budget+stock_sum
# a = Backtest("2017-01-20","2018-01-20",1,2000000,3)
# print(a.run())

start = time.time()
stock = ""

for i in range(200):
    stock = StockPrice.objects.get(code="005930")

print("몽고 접근 : " , (time.time()-start))

start = time.time()
md = ""
for i in range(200):
    md = model_to_dict(stock)

print("모델 투 딕트 : ",(time.time()-start))

start = time.time()
df=""
for i in range(200):
    df = pd.DataFrame(md['data'])

print("데이터 프레임 : ",(time.time()-start))

start = time.time()
r=""
for i in range(200):
    r = df.loc[df['time'] == "2018-03-04"]

print("날짜 탐색 : ",(time.time()-start))