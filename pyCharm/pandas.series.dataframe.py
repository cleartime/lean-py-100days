import numpy as np
import pandas as pd
from pandas import Series, DataFrame

s1 = Series([1,2,3], index=['a','b','c'])
s2 = Series([4,5,6,7], index=['b','c','d','e'])
# print(s1+s2)
d1 = DataFrame(np.arange(4).reshape(2,2), index=['a','b'], columns=['bj','sh'])
d2 = DataFrame(np.arange(9).reshape(3,3), index=['a','b','c'], columns=['bj','sh','ah'])
# print(d1+d2)
d3 = DataFrame([[1,2,3],[4,5,np.nan],[7,8,9]],index=['a','b','c'],columns=['c1','c2','c3'])
print(d3.sum())
print(d3.sum(axis = 1))
print(d3.min())
print(d3.min(axis = 1))
print(d3.describe())
