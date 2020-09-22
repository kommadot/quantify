import pymongo
from pymongo.cursor import CursorType
import json
from collections import OrderedDict


myclient = pymongo.MongoClient("mongodb://j3a105.p.ssafy.io:27017/")
mydb = myclient.testdb
mycol = mydb.testdb
docs = (mycol.find_one())
# print(docs['data'])
# result = mycol.find({'code': '041440'}) # code 안에 차트에 넣고싶은 코드번호
# for i in result:
#     print(i['code'])
 
file_data = OrderedDict()
with open('temporary-static-data.json', 'w', encoding="utf-8") as make_file:
    file_data = docs['data']
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
