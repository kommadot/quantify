import json
from collections import OrderedDict


file_data = OrderedDict()



file_data["{일시}"] = {"open": "2020-09-15", "close":"20000", "high": "10000", "low": "10000", "volume": "10000"}


with open('make.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")