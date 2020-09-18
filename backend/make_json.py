import json
from collections import OrderedDict
import csv


file_data = OrderedDict()
f = open('Value.csv', 'r', encoding='utf=8')
rdr = csv.reader(f)
with open('Value.json', 'w', encoding="utf-8") as make_file:
    for line in rdr:
        # 종목,ROA,CFO,ROA_DIFF,ACCRUAL,LIQUID,MARGIN,TURN,SUM
        file_data[line[1]] = {"ROA": line[2], "CFO":line[3], "ROA_DIFF": line[4], "ACCRUAL": line[5], "LIQUID": line[6], "MARGIN": line[7], "TURN": line[8], "SUM": line[9]}
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")

f.close()   