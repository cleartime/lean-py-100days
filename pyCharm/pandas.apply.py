import pandas as pd
import numpy as np
from pandas import Series, DataFrame

csv = pd.read_csv('./df1.csv')
s1 = Series(['a']*7978)
csv['a'] = s1
def test(a):
    return a+'_abc'
csv['a'] = csv['a'].apply(test)