# 네이버 api를 통한 원하는 주식의 일자별 종가, 전일비, 시가, 고가, 저가, 거래량 데이터 수집

import pandas as pd
import numpy as np
from tabulate import tabulate

import requests
from bs4 import BeautifulSoup

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "backend.settings") 
import django 
django.setup()

from strategy.models import Momentum
from strategy.models import RiskMomentum


def get_url(item_name, code_df):
    code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False)
    url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code.strip())
    return url


code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)
code_df = code_df[['회사명', '종목코드']]
code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})

vari = pd.DataFrame(columns=['종목', '변동성'])
accum_profit = pd.DataFrame(columns=['종목', '누적수익률'])
risk_adj = pd.DataFrame(columns=['종목', '위험조정수익률'])

# for cnt in range(len(code_df)):
for cnt in range(20):
    item_name = code_df.loc[cnt, 'name']
    print(item_name)
    cnt += 1

    url = get_url(item_name, code_df)


    df = pd.DataFrame()

    pg_url = '{url}&page=1'.format(url=url)
    result = requests.get(pg_url)
    bs_obj = BeautifulSoup(result.content, 'html.parser')

    page_cnt = str(bs_obj.find('td', {'class': 'pgRR'}))
    start_idx = page_cnt.find('page') + 5
    end_idx = page_cnt.find('맨뒤') - 2
 
    try:
        end_page = int(page_cnt[start_idx:end_idx])
    except ValueError:
        pass

    # continue
    # 1페이지에서 26페이지(대략 1년)의 데이터만 가져오기
    end_page = end_page if end_page <26 else 26
    for page in range(1, end_page):
        pg_url = '{url}&page={page}'.format(url=url, page=page)
        df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True)
        
    # df.dropna()를 이용해 결측값 있는 행 제거
    df = df.dropna()

    # 한글로 된 컬럼명을 영어로 바꿔줌
    df = df.rename(columns= {'날짜': 'date', '종가': 'close', '전일비': 'diff', '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'})

    # 데이터의 타입을 int형으로 바꿔줌
    df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[['close', 'diff', 'open', 'high', 'low', 'volume']].astype(int)

    # 컬럼명 'date'의 타입을 date로 바꿔줌
    df['date'] = pd.to_datetime(df['date'])

    price = df['close']


    price_profit = price.pct_change()


    # 변동성
    price_variability = price_profit.std() * np.sqrt(len(df))

    # 누적수익률
    accumulated_price_profit = price_profit + 1
    accumulated_price_profit = np.cumprod(accumulated_price_profit)
    accumulated_price_profit = accumulated_price_profit.iloc[-1]
    accumulated_price_profit = accumulated_price_profit - 1
    print(accumulated_price_profit)
    accum_profit.loc[cnt, ['종목']] = item_name
    accum_profit.loc[cnt, ['누적수익률']] = accumulated_price_profit

    # 위험조정수익률(누적수익률/변동성)
    risk_adjust_profit = accumulated_price_profit / price_variability
    print(risk_adjust_profit)
    risk_adj.loc[cnt, ['종목']] = item_name
    risk_adj.loc[cnt, ['위험조정수익률']] = risk_adjust_profit


vari = vari.sort_values(by=["변동성"], ascending=[True])


accum_profit = accum_profit.sort_values(by=["누적수익률"], ascending=[False])
print(accum_profit)

risk_adj = risk_adj.sort_values(by=["위험조정수익률"], ascending=[False])
print(risk_adj)


df_records = accum_profit.head(10).to_dict('records')

df_records2 = risk_adj.head(10).to_dict('records')


model_instances = [Momentum(
    name=record['종목'],
    momentum=record['누적수익률'],
) for record in df_records]

Momentum.objects.all().delete()
Momentum.objects.bulk_create(model_instances)


model_instances2 = [RiskMomentum(
    name=record['종목'],
    risk_momentum=record['위험조정수익률'],
) for record in df_records2]

RiskMomentum.objects.all().delete()
RiskMomentum.objects.bulk_create(model_instances2)

