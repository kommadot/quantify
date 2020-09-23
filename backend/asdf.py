import pandas as pd
import pandas_read_xml as pdx
from urllib.request import urlopen
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup 

url = "https://fchart.stock.naver.com/sise.nhn?symbol=005930&timeframe=day&count=8005&requestType=0"
response = urlopen(url).read()
a = BeautifulSoup(response,'lxml-xml')
df_col = ['date','s','e','u','r','q']

rows = []
for node in a.find_all('item'):
    # print(node['data'])
    rows.append(node['data'].split("|"))
    # n_title = node.find("TITLE").text
    # n_artist = node.find("ARTIST").text
    # n_country = node.find("COUNTRY").text
    # n_company = node.find("COMPANY").text
    # n_price = node.find("PRICE").text
    # n_year = node.find("YEAR").text
    # rows.append({"title": n_title, 

    #              "artist": n_artist, 

    #              "country": n_country, 

    #              "company": n_company, 

    #              "price": n_price, 

    #              "year": n_year})
# print(rows)
df = pd.DataFrame(rows,columns=df_col)
print(df)
# a = pdx.read_xml("https://fchart.stock.naver.com/sise.nhn?symbol=005930&timeframe=day&count=8005&requestType=0")
# print(a)