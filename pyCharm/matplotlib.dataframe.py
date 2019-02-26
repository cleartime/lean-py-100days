import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

df = DataFrame(
    np.random.randint(1,10,40).reshape(10,4),
    columns=['a','b','c','d']
)
# df.plot(kind='area', stacked=True)
# for i in df.index:
#     df.iloc[i].plot(label=str(i))
# plt.legend()
# plt.show()

s = Series(np.random.randn(1000))
# plt.hist(s)
a = np.arange(10)

# plt.hist(df)
# plt.show()
# re = plt.hist(s, rwidth=0.9, bins=200, color='r')
# s.plot(kind='kde')
plt.show()
