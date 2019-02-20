import numpy as np
import pandas as pd
from pandas import Series, DataFrame

s1 = Series(np.random.randn(10))
s2 = s1.sort_values(ascending=False)
s3 = s2.sort_index()
# print(s1)
# print(s2)
# print(s3)

d1 = DataFrame(np.random.randn(40).reshape(8,5), columns=['a','b','c','d','e'])
d2 = d1.sort_values('a', ascending=False)
d3 = d2.sort_index()
# print(d1)
# print(d2)
# print(d3)


cvsurl = './df1.csv'
d4 = pd.read_csv(cvsurl)[['Language']].sort_values('Language', ascending=False)
# d4.to_csv('df2.csv')


d5 = DataFrame(np.arange(9).reshape(3,3,), index=['bj','sh','ah'], columns=['a','b','c'])
# d5.index = Series(['bj','sh','sc'])
# d5.index = d5.index.map(str.upper)
# d5.rename(index = str.lower, columns = str.upper)
d6 = d5.rename(index={'bj':'beigin'}, columns = {'a':'aa'})