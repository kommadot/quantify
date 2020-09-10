import pandas as pd
from FinancialStatement import FinancialStatement
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)
code_df = code_df[['회사명', '종목코드']]
code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})

# value_df = pd.DataFrame(columns=['종목', 'PER', 'PBR', 'PCR', 'PSR'])
value_df = pd.DataFrame(columns=['종목', 'PER', 'PBR'])

for cnt in range(5):
    item_name = code_df.loc[cnt, 'name']
    code = code_df.loc[cnt, 'code']
    fs = FinancialStatement(code)
    cnt += 1
    value_df.loc[cnt, ['종목']] = item_name
    value_df.loc[cnt, ['PER']] = fs.get_PER()
    value_df.loc[cnt, ['PBR']] = fs.get_PBR()
    # value_df.loc[cnt, ['PCR']] = fs.get_PCR()
    # value_df.loc[cnt, ['PSR']] = fs.get_PSR()

value_df['PER'] = value_df['PER'].rank(axis=0)
value_df['PBR'] = value_df['PBR'].rank(axis=0)
print(tabulate(value_df, headers='keys', tablefmt='psql'))