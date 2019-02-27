# 基本信息
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# 股票数据的读取
import pandas_datareader as pdr

# 可视化
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import  datetime

start  = datetime(2015,9,20)
alibaba = pdr.get_data_yahoo('BABA', start = start)
amazon = pdr.get_data_yahoo('AMZN', start = start)

# alibaba.to_csv('./baba.csv')
# amazon.to_csv('./amazon.csv')

# alibaba['Adj Close'].plot(legend=True)
# amazon['Adj Close'].plot(legend=True)
# alibaba['high-low'] = alibaba['High'] - alibaba['Low']
# alibaba['high-low'].plot(legend=True)
alibaba['daily-return'] = alibaba['Adj Close'].p ct_change()
alibaba['daily-return'].plot(figsize = (10, 4), linestyle='--', marker='.')
sns.distplot(alibaba['daily-return'].dropna(),bins=100,color='purple')
plt.show()