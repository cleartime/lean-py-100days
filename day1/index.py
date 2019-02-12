import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer

dataset = pd.read_csv('data.csv')
X = dataset.iloc[ : , :-1].values
Y = dataset.iloc[ : , 3].values

imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[ : , 1:3])
X[ : , 1:3] = imputer.transform(X[ : , 1:3])

print(X)
print(Y)