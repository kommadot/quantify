from pymongo import MongoClient
import pymongo
from pymongo.cursor import CursorType
import csv
import json

# host = "localhost"
# port = "27017"
# mongo = MongoClient(host, int(port))
# print(mongo)
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
#db이름
mydb = myclient.testdb

print(mydb.collection_names())
#테이블이름
mycol = mydb.testdb

def insert_item_one(mongo, data, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_one(data).inserted_id
    return result

def insert_item_many(mongo, datas, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_many(datas).inserted_ids
    return result
    

#print(mongo)

with open('make.json') as json_file:
    json_data = json.load(json_file)
    # json_object = json_data["2020-09-16"]
# print(mydb.list_collection_names())

mycol.insert_one(json_data)