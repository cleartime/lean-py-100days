import numpy as np
import pandas as pd
from pandas import Series, DataFrame

l1 = np.random.randint(32,100,size=20)
bs = [0,59,70,80,100]

d1 = pd.cut(l1, bs)
d2 = pd.value_counts(d1)

df = DataFrame()
df['score'] = l1
df['student'] = [pd.util.testing.rands(3) for i in range(20)]
df['categories'] = pd.cut(df['score'], bs, labels=['low','ok','good','greate'])
