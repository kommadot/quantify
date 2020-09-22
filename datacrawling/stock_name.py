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
mydb = myclient.stockinfo
mycol = mydb.stockinfo
code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)
code_df = code_df[['회사명', '종목코드']]
code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})
# print(code_df['name'])


file_data = OrderedDict()
# file_data2 = OrderedDict()
for i in range(len(code_df)):
    # print(code_df['name'][i])
    with open('test.json', 'w', encoding="utf-8") as make_file:
        # file_data['stock'] = {"name": code_df['name'][i], "code": code_df['code'][i]}
        file_data['code']=code_df['code'][i]
        file_data['name'] = code_df['name'][i]
        json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
    with open('test.json', encoding='UTF8') as json_file:
        json_data = json.load(json_file)
    mycol.insert_one(json_data)





    


