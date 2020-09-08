import pandas as pd
import numpy as np

price = pd.read_csv('FinancePrice.csv')
price = price['close']

price_interest = price.pct_change()
# print(price_interest)

price_variability = price_interest.std() * np.sqrt(250)
print(price_variability)