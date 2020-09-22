import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup 
from collections import OrderedDict
# from pymongo import MongoClient
import pymongo
import json
from pymongo.cursor import CursorType


def get_url(item_name, code_df):
    code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False)
    url = "https://fchart.stock.naver.com/sise.nhn?symbol={code}&timeframe=day&count=8005&requestType=0".format(code=code.strip())
    return url


def insert_item_one(mongo, data, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_one(data).inserted_id
    return result


def insert_item_many(mongo, datas, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_many(datas).inserted_ids
    return result

# myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
myclient = pymongo.MongoClient("mongodb://j3a105.p.ssafy.io:27017/")
mydb = myclient.testdb
mycol = mydb.testdb
code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)
code_df = code_df[['회사명', '종목코드']]
code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})

def get_price_1y(item_name,i):
    code = code_df.code[i]
    url = get_url(item_name, code_df)
    response = urlopen(url).read()
    # print(url)
    a = BeautifulSoup(response,'lxml-xml')
    #일자/시가/고가/저가/종가/거래량
    df_col = ['date','s','e','u','r','q']
    rows = []
    file_data = OrderedDict()
    daterows = OrderedDict()
    
    for node in a.find_all('item'):
        rows.append(node['data'].split("|"))

    df = pd.DataFrame(rows,columns=df_col)
    # print(df)
    with open(item_name+'.json', 'w', encoding="utf-8") as make_file:

        for line in rows:
            # print(line)
            # str(line)close,diff,open,high,low,volume
            date = line[0][:4] + '-' + line[0][4:6] + '-' + line[0][6:]
            daterows[date] = {"open": line[1], "high":line[2], "low": line[3], "close": line[4], "volume": line[5]}
        file_data['data'] = daterows
        file_data["code"] = code
        json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
    with open(item_name + '.json') as json_file:
        json_data = json.load(json_file)
    # json_object = json_data["2020-09-16"]
    mycol.insert_one(json_data)


for i in range(len(code_df)):
    # print(i)
    get_price_1y(code_df.name[i], i)