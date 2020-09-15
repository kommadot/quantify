import pandas_datareader as pdr



#pdr.get_data_yahoo('종목 코드', start='시작 시점', end='종료 시점')
smasung = pdr.get_data_yahoo('005930.KS', start='2011-08-19', end='2020-09-09')
print(smasung)