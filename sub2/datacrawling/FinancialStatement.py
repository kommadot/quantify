import requests
import re
import pandas as pd

class FinancialStatement:
    def __init__(self,code):
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

    def get_all(self):
        return self.financial_statement

    def get_PER(self):
        return self.finalcial_statement[self.finalcial_statement.columns[-1]].loc['PER(배)']

    def get_PBR(self):
        return self.finalcial_statement[self.finalcial_statement.columns[-1]].loc['PBR(배)']

    def get_ROA(self):
        return self.finalcial_statement[self.finalcial_statement.columns[-1]].loc['ROA(%)']

    def get_ROE(self):
        return self.finalcial_statement[self.finalcial_statement.columns[-1]].loc['ROE(%)']
