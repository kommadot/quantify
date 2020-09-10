import pandas as pd
from FinancialStatement import FinancialStatement
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)
code_df = code_df[['회사명', '종목코드']]
code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})

value_df = pd.DataFrame(columns=['종목', 'ROA', 'CFO', 'ROA_DIFF', 'ACCRUAL', 'EQ_OFFER', 'TURN', 'SUM'])

for cnt in range(len(code_df)):
# for cnt in range(250, 301):
    item_name = code_df.loc[cnt, 'name']
    code = code_df.loc[cnt, 'code']
    try:
        fs = FinancialStatement(code)
    except KeyError:
        continue
    cnt += 1
    value_df.loc[cnt, ['종목']] = item_name
    value_df.loc[cnt, ['ROA']] = 1 if fs.get_ROA() > 0 else 0
    value_df.loc[cnt, ['CFO']] = 1 if fs.get_CFO() > 0 else 0
    value_df.loc[cnt, ['ROA_DIFF']] = 1 if fs.get_ROA_DIFF() > 0 else 0
    value_df.loc[cnt, ['ACCRUAL']] = 1 if fs.get_CFO() > fs.get_ROA() else 0
    value_df.loc[cnt, ['EQ_OFFER']] = 1 if fs.get_EQ_OFFER() <= 0 else 0
    value_df.loc[cnt, ['TURN']] = 1 if fs.get_TURN() > 0 else 0

value_df['SUM'] = value_df[['ROA', 'CFO', 'ROA_DIFF', 'ACCRUAL', 'EQ_OFFER', 'TURN']].sum(axis=1)
value_df = value_df.sort_values(by=["SUM"], ascending=[False])
print(tabulate(value_df, headers='keys', tablefmt='psql'))
print(len(value_df))
value_df.to_csv('./Q.csv')