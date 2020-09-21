# 네이버 api를 통한 원하는 주식의 일자별 종가, 전일비, 시가, 고가, 저가, 거래량 데이터 수집

import pandas as pd
import numpy as np
from tabulate import tabulate

import requests
from bs4 import BeautifulSoup


def get_url(item_name, code_df):
    code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False)
    url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code.strip())
    return url


code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)
code_df = code_df[['회사명', '종목코드']]
code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})

# print(code_df.name[1])
# print(code_df.code[1])
def get_price_1y(item_name, i):
    code = code_df.code[i]
    print(code, i)
    # 신라젠의 일자데이터 url 가져오기
    url = get_url(item_name, code_df)
    # print(code_df)


    # 일자 데이터를 담을 df라는 DataFrame 정의
    df = pd.DataFrame()
    pg_url = '{url}&page=1'.format(url=url)
    result = requests.get(pg_url)
    bs_obj = BeautifulSoup(result.content, 'html.parser')
    page_cnt = str(bs_obj.find('td', {'class': 'pgRR'}))
    start_idx = page_cnt.find('page') + 5
    end_idx = page_cnt.find('맨뒤') - 2
    # print(page_cnt[start_idx:end_idx])
    # print(page_cnt)
    end_page = int(page_cnt[start_idx:end_idx])
    # print(end_page)
    # print(end_idx)

    # continue
    # 1페이지에서 26페이지(대략 1년)의 데이터만 가져오기
    end_page = end_page if end_page <80 else 80
    for page in range(1, end_page):
        pg_url = '{url}&page={page}'.format(url=url, page=page)
        # print(pg_url, page)
        df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True)
        # print(df)

        
    # df.dropna()를 이용해 결측값 있는 행 제거
    df = df.dropna()

    # 한글로 된 컬럼명을 영어로 바꿔줌
    df = df.rename(columns= {'날짜': 'date', '종가': 'close', '전일비': 'diff', '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'})

    # 데이터의 타입을 int형으로 바꿔줌
    df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[['close', 'diff', 'open', 'high', 'low', 'volume']].astype(int)

    # 컬럼명 'date'의 타입을 date로 바꿔줌
    df['date'] = pd.to_datetime(df['date'])

    # print(tabulate(df, headers='keys', tablefmt='psql'))

    df.to_csv('./' + code + '.csv')


for i in range(116, len(code_df)):
    print(i)
    get_price_1y(code_df.name[i], i)