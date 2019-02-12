import numpy as np
import pandas as pd

dataset = pd.read_csv('data.csv')
X = dataset.iloc[ : , :-1].values
Y = dataset.iloc[ : , 3].values

print(X)
print(Y)