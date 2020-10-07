import pandas as pd
from FS import FS
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "backend.settings") 
import django 
django.setup()

from strategy.models import Value

import math

code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)
code_df = code_df[['회사명', '종목코드']]
code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})

value_df = pd.DataFrame(columns=['종목', 'code', 'PER', 'PBR', 'PSR'])

for cnt in range(len(code_df)):
# for cnt in range(20):
    item_name = code_df.loc[cnt, 'name']
    code = code_df.loc[cnt, 'code']
    # print(fs.get_PER())
    
    try:
        fs = FS(code)
        if fs.get_SC() < 10000:
            continue
        if math.isnan(fs.get_PER()) or math.isnan(fs.get_PBR()) or math.isnan(fs.get_PSR()):
            continue
        cnt += 1
        print(item_name)
        value_df.loc[cnt, ['종목']] = item_name
        value_df.loc[cnt, ['code']] = code
        value_df.loc[cnt, ['PER']] = fs.get_PER()
        value_df.loc[cnt, ['PBR']] = fs.get_PBR()
        value_df.loc[cnt, ['PSR']] = fs.get_PSR()
    except:
        continue


value_df['PERRANK'] = value_df['PER'].rank(axis=0)
value_df['PBRRANK'] = value_df['PBR'].rank(axis=0)
value_df['PSRRANK'] = value_df['PSR'].rank(axis=0)
# print(tabulate(value_df, headers='keys', tablefmt='psql'))

value_df['RANK'] = value_df.apply(lambda row: (row['PERRANK'] + row['PBRRANK'] + row['PSRRANK']),axis=1)
# value_df['RANK'] = value_df[['PER', 'PBR', 'PSR']].sum(axis=1)
value_df = value_df.sort_values(by=["RANK"], ascending=[True])
value_df = value_df[['종목', 'code', 'PER', 'PBR', 'PSR','RANK']]


df_records = value_df.to_dict('records')

print(df_records)

model_instances = [Value(
    name=record['종목'],
    code=record['code'],
    per=record['PER'],
    pbr=record['PBR'],
    psr=record['PSR'],
    rank=record['RANK']
) for record in df_records]

Value.objects.all().delete()
Value.objects.bulk_create(model_instances)