import numpy as np
import pandas as pd
s1 = pd.Series([1,2,3,4])
# print(s1)
# print(s1.values)
# print(s1.index)
s2 = pd.Series(np.arange(10))
# print(s2)
# print(s2.values)
# print(s2.index)
s3 = pd.Series({'a':1,'b':2,'c':3})
# print(s3)
# print(s3.values)
# print(s3.index)
s4 = pd.Series([1,2,3,4],index = ['a','b','c','d'])
# print(s4)
# print(s4.values)
# print(s4.index)
# print(s4['a'])
# print(s4[s4>2])
# print(s4.to_dict())
index1 = ['a','b','c','d','e']
s5 = pd.Series(s4,index = index1)
# print(pd.isnull(s5))
# print(pd.notnull(s5))
s5.name = 'demo'
s5.index.name = 'deme instaz'
# print(s5)
print(s5.values)