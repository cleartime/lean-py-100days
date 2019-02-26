import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import seaborn as sns

s1 = Series(np.random.randn(1000))
s2 = Series(np.random.randn(1000))
# s1.plot(kind='kde')
# plt.hist(s1)
# plt.show()

# sns.distplot(s1, hist=True, kde=True)
# sns.kdeplot(s1, shade=True, color='r')
d1 = DataFrame([s1,s2])
d2 = d1.head()
sns.heatmap(d2)
plt.show()
