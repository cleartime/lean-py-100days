import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import webbrowser
link = 'https://www.tiobe.com/tiobe-index/'
# webbrowser.open(link)


df = pd.read_clipboard()
# print(df)
df_new = DataFrame(df, columns=['Programming Language', 'Feb 2018', 'safsf'])
df_new['safsf'] = pd.Series(np.arange(0,20))
print(df_new)



