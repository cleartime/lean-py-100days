import numpy as np
import pandas as pd
from pandas import Series, DataFrame


data = {
    'Country': ['Belgium', 'India', 'Brazil'],
    'Capital': ['Brussels', 'New Delhi', 'Brasilia'],
    'Population': [1324214, 324235234, 43543534]
}


df = DataFrame(data)
s1 = Series(data['Country'])
s2 = Series(data['Capital'])
s3 = Series(data['Population'])
df_new = pd.DataFrame([s1,s2,s3], index = ['a','b','c']).T
print(df_new)