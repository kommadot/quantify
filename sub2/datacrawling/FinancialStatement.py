import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime

class FinancialStatement:
    def __init__(self,code):
        self.now = datetime.datetime.now()
        self.cur_index = str(self.now.year-1) + "/12"
        self.url="https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd="

        result = requests.get(self.url + code)
        pattern_enc = re.compile("encparam: '(.+)'", re.IGNORECASE)
        pattern_id = re.compile("id: '(.+?)'", re.IGNORECASE)

        target_text = result.text
        encparam = pattern_enc.search(target_text).groups()[0]
        id_ = pattern_id.search(target_text).groups()[0]

        payload = {}
        payload['cmp_cd'] = code
        payload['fin_typ'] = 4
        payload['freq_typ'] = 'Y'
        payload['encparam'] = encparam
        payload['id'] = id_

        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Referer': "https://navercomp.wisereport.co.kr/v2/company/ajax/cF1001.aspx?",
            'X-Requested-With': 'XMLHttpRequest'
        }

        finacial_url = "https://navercomp.wisereport.co.kr/v2/company/ajax/cF1001.aspx?"
        r = requests.get(finacial_url, params=payload, headers=head)

        financial_statement = pd.read_html(r.text)[1]
        financial_statement.columns = financial_statement.columns.get_level_values(1)
        financial_statement = financial_statement.dropna(axis=1, how='all')
        financial_statement.rename(columns=lambda x: x.replace("(IFRS연결)", "").replace(" ", ""), inplace=True)

        financial_statement.set_index(financial_statement.columns[0], inplace=True)

        self.finalcial_statement = financial_statement
        url = 'https://finance.naver.com/item/main.nhn?code='+code
        result = requests.get(url)
        bs_obj = BeautifulSoup(result.content, 'html.parser')

        # 시가총액
        market_sum = bs_obj.find('em', {'id': '_market_sum'})
        self.market_sum = int(
            market_sum.text.replace(" ", "").replace("\t", "").replace("\n", "").replace("조", "").replace(",",
                                                                                                          "").strip()) * 100000000

        self.cur_price = bs_obj.find('p', {'class': 'no_today'}).text.replace(",", "").split()[0]
        self.finalcial_statement.to_csv("F.csv")

    def get_all(self):
        return self.financial_statement

    def get_PER(self):
        return self.finalcial_statement[self.cur_index].loc['PER(배)']

    def get_PBR(self):
        return self.finalcial_statement[self.cur_index].loc['PBR(배)']

    def get_ROA(self):
        return self.finalcial_statement[self.cur_index].loc['ROA(%)']

    def get_ROE(self):
        return self.finalcial_statement[self.cur_index].loc['ROE(%)']

    def get_PCR(self):
        return self.market_sum / self.finalcial_statement[self.cur_index].loc['영업활동현금흐름']

    def get_PSR(self):
        income = int(self.finalcial_statement[self.cur_index].loc['매출액']) * 100000000
        stock_num = int(self.finalcial_statement[self.cur_index].loc['발행주식수(보통주)'])
        sps = income/stock_num
        return self.cur_price / sps