import numpy as np
import pandas as pd
from pandas import Series, DataFrame


import webbrowser
df1 = pd.read_clipboard()
# df2 = pd.read_excel('1.xlsx')
# df1.to_csv('df1.csv', index=False)
df2 = pd.read_csv('df1.csv')