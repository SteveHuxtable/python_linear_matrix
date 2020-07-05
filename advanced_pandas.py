import numpy as np
import pandas as pd

values = pd.Series([0, 1, 0, 0] * 2)
dim = pd.Series(['apple', 'orange'])

s = pd.Series(['a', 'b', 'c', 'd'] * 2)
cat_s = s.astype('category')
cat_s.cat
cat_s.cat.codes
cat_s.cat.categories

actual_categories = ['a', 'b', 'c', 'd', 'e']

df = pd.DataFrame({'key': ['a', 'b', 'c', 'd'] * 3,
                   'value': np.arange(12.)})

N = 15
times = pd.date_range('2017-05-20 00:00', freq='1min', periods=N)
df = pd.DataFrame({'time': times,
                   'value': np.range(N)})

df.set_index('time').resample('5min').count()