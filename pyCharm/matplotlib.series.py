import numpy as np
import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt
s1 = Series(np.random.randn(10)).cumsum()
s2 = Series(np.random.randn(10)).cumsum()
s2.plot(label='s2')
# s1.plot()
s1.plot(label='s1', title='this is series', style='--')
plt.legend()
plt.show()