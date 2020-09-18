import json
from collections import OrderedDict
import csv


file_data = OrderedDict()
f = open('price_1y.csv', 'r', encoding='utf=8')
file_data[name] = {}
rdr = csv.reader(f)
with open('make.json', 'w', encoding="utf-8") as make_file:
    for line in rdr:
        # print(line[0])
        # str(line)close,diff,open,high,low,volume
        file_data[line[1]] = {"close": line[2], "diff":line[3], "open": line[4], "high": line[5], "low": line[6], "volume": line[7]}
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")

f.close()   
