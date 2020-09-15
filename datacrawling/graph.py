import json
from collections import OrderedDict


file_data = OrderedDict()

file_data["name"] = "Graph"
file_data["language"] = "kor"
file_data["words"] = {"일시": "2020-09-15", "종가":"20000", "시가": "10000"}
file_data["number"] = 3

with open('Graph.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")