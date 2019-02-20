import numpy as np
import pandas as pd
from pandas import Series, DataFrame

arr1 = np.arange(9).reshape(3,3)
arr2 = np.arange(9).reshape(3,3)
arr3 = np.concatenate( [arr1,arr2], axis=1)

s1 = Series([1,2,3],index=['x','y','z'])
s2 = Series([4,5],index=['a','b'])
s3 = np.concatenate([s1, s2])
s4 = pd.concat([s1,s2])

d1 = DataFrame(np.random.randn(4,3), columns=['x','y','z'])
d2 = DataFrame(np.random.randn(3,3), columns=['a','b','c'])
d3 = pd.concat([d1,d2])


# combine

ss1 = Series([2, np.nan,4,np.nan], index=['a','b','c','d'])
ss2 = Series([1,2,3,4], index=['a','b','c','d'])
ss3 = ss1.combine_first(ss2)
dd1 = DataFrame({
    'x':[1,np.nan,4,np.nan],
    'y':[3,np.nan,5,np.nan]
})
dd2 = DataFrame({
    'x':[1,2,3,4],
    'y':[np.nan,5,np.nan,7]
})
dd3 = dd1.combine_first(dd2)