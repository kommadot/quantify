from bs4 import BeautifulSoup 
from tabulate import tabulate
import re
import requests 
import pandas as pd
import datetime


class FS:
    def __init__(self, code):
        self.now = datetime.datetime.now()
        self.cur_index = str(self.now.year-1) + "/12"
        self.past_index = str(self.now.year-2) + "/12"

        self.url1 = f'http://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&gicode=A{code}'
        self.fs_lists1 = pd.read_html(self.url1)

        self.fs_list1_HH = self.fs_lists1[4]
        self.fs_list1_HH.set_index(self.fs_list1_HH.columns[0], inplace=True)
        self.fs_list1_HH[self.cur_index]
        self.fs_list1_HH[self.past_index]

        self.fs_list1_PS = self.fs_lists1[0]
        self.fs_list1_PS.set_index(self.fs_list1_PS.columns[0], inplace=True)
        self.fs_list1_PS[self.cur_index]
        self.fs_list1_PS[self.past_index]

        self.fs_list1_JS = self.fs_lists1[2]
        self.fs_list1_JS.set_index(self.fs_list1_JS.columns[0], inplace=True)
        self.fs_list1_JS[self.cur_index]
        self.fs_list1_JS[self.past_index]


        self.url2 = f'http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A{code}'
        self.fs_lists2 = pd.read_html(self.url2)

        self.fs_list2_SH = self.fs_lists2[0]
        self.fs_list2_SH.set_index(self.fs_list2_SH.columns[0], inplace=True)
        # self.fs_list2_SH[self.cur_index]
        # self.fs_list2_SH[self.past_index]

        self.fs_list2_FH = self.fs_lists2[11]
        self.fs_list2_FH.columns = self.fs_list2_FH.columns.get_level_values(1)
        self.fs_list2_FH.set_index(self.fs_list2_FH.columns[0], inplace=True)
        self.fs_list2_FH[self.cur_index]
        self.fs_list2_FH[self.past_index]

    ############################################

    def get_PER(self):
        return self.fs_list2_FH[self.cur_index].loc['PER']


    def get_PBR(self):
        return self.fs_list2_FH[self.cur_index].loc['PBR']


    def SC(self):
        return int(self.fs_list2_SH[1].loc['시가총액(보통주,억원)'])

    # 시가총액 / 매출액
    def get_PSR(self):
        return int(self.fs_list2_SH[1].loc['시가총액(보통주,억원)']) / self.fs_list1_PS[self.cur_index].loc['매출액']

    ############################################

    def get_ROA(self):
        return self.fs_list2_FH[self.cur_index].loc['ROA']


    # 영업활동현금흐름 / 총자산
    def get_CFO(self):
        return self.fs_list1_HH[self.cur_index].loc['영업활동으로인한현금흐름'] / self.fs_list1_JS[self.cur_index].loc['자산']


    def get_ROA_DIFF(self):
        return self.fs_list2_FH[self.cur_index].loc['ROA'] - self.fs_list2_FH[self.past_index].loc['ROA']
    
    
    # def get_LEVER(self):
    #     return self.fs_list1_JS[self.cur_index].loc[]


    def get_LIQUID_cur(self):
        return self.fs_list1_JS[self.cur_index].loc['유동자산계산에 참여한 계정 펼치기'] / self.fs_list1_JS[self.cur_index].loc['유동부채계산에 참여한 계정 펼치기']
    
    def get_LIQUID_past(self):
        return self.fs_list1_JS[self.past_index].loc['유동자산계산에 참여한 계정 펼치기'] / self.fs_list1_JS[self.past_index].loc['유동부채계산에 참여한 계정 펼치기']


    # def get_EQ_OFFER(self):
    #     return self.finalcial_statement[self.cur_index].loc['발행주식수(보통주)'] - self.finalcial_statement[self.past_index].loc['발행주식수(보통주)']


    def get_MARGIN_cur(self):
        return self.fs_list1_PS[self.cur_index].loc['매출총이익'] / self.fs_list1_PS[self.cur_index].loc['매출액']

    def get_MARGIN_past(self):
        return self.fs_list1_PS[self.past_index].loc['매출총이익'] / self.fs_list1_PS[self.past_index].loc['매출액']


    def get_TURN_cur(self):
        return self.fs_list1_PS[self.cur_index].loc['매출액'] / self.fs_list1_JS[self.cur_index].loc['자산']

    def get_TURN_past(self):
        return self.fs_list1_PS[self.past_index].loc['매출액'] / self.fs_list1_JS[self.past_index].loc['자산']


    def get_ROE(self):
        return self.fs_list2_FH[self.cur_index].loc['ROE']