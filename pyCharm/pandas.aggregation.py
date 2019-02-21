import numpy as np
import pandas as pd
from pandas import Series, DataFrame


s1 = DataFrame(np.random.randint(0,10,9,dtype='int').reshape (3,3), index=['a','b','c'],columns=['d','e','f'])