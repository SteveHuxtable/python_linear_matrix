import numpy as np
import pandas as pd

test_df = pd.DataFrame(np.arange(3 * 6).reshape((3, 6)), index=['a', 'b', 'c'])
test_df.stack()

s1 = pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])
data = pd.concat([s1, s2], keys=['one', 'two'])

data2 = pd.concat([s1, s2], axis=1, keys=['a', 'b'])

# pivot length to width
data = pd.read_csv('macrodata.csv')
periods = pd.PeriodIndex(year=data.year, quarter=data.quarter, name='date')
columns = pd.Index(['realgdp', 'infl', 'unemp'], name='item')
data = data.reindex(columns=columns)
data.index = periods.to_timestamp('D', 'end')
data.stack().reset_index().rename(columns={0: 'value'})