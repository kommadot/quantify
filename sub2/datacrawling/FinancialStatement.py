import requests
from bs4 import BeautifulSoup
import sqlite3
import re
import pandas as pd
from tabulate import tabulate

url_tmp = "https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd=005930"
r_tmp = requests.get(url_tmp)

pattern_enc = re.compile("encparam: '(.+)'", re.IGNORECASE)
pattern_id  = re.compile("id: '(.+?)'", re.IGNORECASE)

target_text = r_tmp.text
encparam = pattern_enc.search(target_text).groups()[0]
id_ = pattern_id.search(target_text).groups()[0]

payload = {}
payload['cmp_cd'] = "005930"
payload['fin_typ'] = 4
payload['freq_typ']= 'Y'
payload['encparam'] = encparam
payload['id'] = id_

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Referer' : "https://navercomp.wisereport.co.kr/v2/company/ajax/cF1001.aspx?",
    'X-Requested-With': 'XMLHttpRequest'
}

finacial_url = "https://navercomp.wisereport.co.kr/v2/company/ajax/cF1001.aspx?"
r = requests.get(finacial_url, params=payload, headers=head)

financial_statement = pd.read_html(r.text)[1]

financial_statement.to_csv('./FinancialStatement.csv')
print(financial_statement)