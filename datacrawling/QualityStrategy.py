import pandas as pd
from FS import FS
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)
code_df = code_df[['회사명', '종목코드']]
code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})

value_df = pd.DataFrame(columns=['종목', 'ROA', 'CFO', 'ROA_DIFF', 'ACCRUAL', 'LIQUID', 'MARGIN', 'TURN', 'SUM'])

# for cnt in range(len(code_df)):
for cnt in range(5):
    item_name = code_df.loc[cnt, 'name']
    code = code_df.loc[cnt, 'code']
    try:
        fs = FS(code)
    except KeyError:
        continue
    cnt += 1
    value_df.loc[cnt, ['종목']] = item_name
    value_df.loc[cnt, ['ROA']] = 1 if fs.get_ROA() > 0 else 0
    value_df.loc[cnt, ['CFO']] = 1 if fs.get_CFO() > 0 else 0
    value_df.loc[cnt, ['ROA_DIFF']] = 1 if fs.get_ROA_DIFF() > 0 else 0
    value_df.loc[cnt, ['ACCRUAL']] = 1 if fs.get_CFO() > fs.get_ROA() else 0
    value_df.loc[cnt, ['LIQUID']] = 1 if fs.get_LIQUID_cur() - fs.get_LIQUID_past() > 0 else 0
    value_df.loc[cnt, ['MARGIN']] = 1 if fs.get_MARGIN_cur() - fs.get_MARGIN_past() > 0 else 0
    value_df.loc[cnt, ['TURN']] = 1 if fs.get_TURN_cur() - fs.get_TURN_past() > 0 else 0

value_df['SUM'] = value_df[['ROA', 'CFO', 'ROA_DIFF', 'ACCRUAL', 'LIQUID', 'TURN']].sum(axis=1)
value_df = value_df.sort_values(by=["SUM"], ascending=[False])
print(tabulate(value_df, headers='keys', tablefmt='psql'))
# print(len(value_df))
# value_df.to_csv('./Q.csv')