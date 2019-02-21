import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from datetime import datetime
from matplotlib import pyplot as plt

csv = pd.read_csv('./df1.csv')
s1 = Series(['a']*7978)
csv['a'] = s1
def test(a):
    return a+'_abc'
csv['a'] = csv['a'].apply(test)



t_range = pd.date_range('2019-01-01', '2019-12-30', freq='H')
stock_d = DataFrame(index=t_range)
stock_d['BABA'] = np.random.randint(80,160,size=len(t_range))
stock_d['TX'] = np.random.randint(30,50,size=len(t_range))
stock_d['GXX'] = np.random.randint(130,350,size=len(t_range))
stock_d.plot()
# plt.show()
weekly_d = DataFrame()
weekly_d['BABA'] = stock_d['BABA'].resample('W').mean()
weekly_d['TX'] = stock_d['TX'].resample('W').mean()
weekly_d['GXX'] = stock_d['GXX'].resample('W').mean()
weekly_d.plot()
plt.show()