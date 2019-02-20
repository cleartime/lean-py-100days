import numpy as np
import pandas as pd
from pandas import Series, DataFrame

d1 = DataFrame({'key':['x','y','z'], 'data_set1':[1,2,3]})
d2 = DataFrame({'key':['a','b','c'], 'data_set2':[4,5,6]})
d3 = pd.merge(d1,d2)
d4 = pd.merge(d1,d2, how='left')
d5 = pd.merge(d1,d2, how='right')
d6 = pd.merge(d1,d2, how='outer')
d7 = pd.merge(d1,d2, on='key')