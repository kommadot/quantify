from bs4 import BeautifulSoup 
from tabulate import tabulate
from FS import FS

import requests 
import pandas as pd


# for fs_list in fs_lists2:
#     print(fs_list)
#     print('')
#     print('')

code = '005930'
fs = FS(code)

print(fs.get_PER())
print(fs.get_PBR())
print(fs.get_PSR())
print(fs.get_ROA())
print(fs.get_CFO())
print(fs.get_ROA_DIFF())
print(fs.get_LIQUID())
print(fs.get_MARGIN())
print(fs.get_TURN())