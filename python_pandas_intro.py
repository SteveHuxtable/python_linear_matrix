import pandas as pd
import numpy as np
from pandas import Series, DataFrame

obj = Series([1, 2, -3, 4])
obj.index

sdata = {'a':0, 'b':1, 'c':2}
obj2 = Series(sdata)

obj2[['b', 'c', 'a']]

obj2.name = "hu"
obj2.index.name = 'alpha'

# create a DataFrame
test_df = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
test_df = pd.DataFrame(test_df, columns=['b', 'a', 'c'])
test_df.loc[[2, 1, 0]]

del test_df['a']

obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3.reindex(range(6), method='ffill')

frame = pd.DataFrame(np.arange(9).reshape((3, 3), order='A'), index=['a', 'b', 'c'], columns=['Ohio', 'Texas', 'California'])
frame2 = frame.reindex(['a', 'b', 'c', 'd'])

frame2.loc[['a'], ['Ohio']]
frame2['Ohio']['a']



frame3 = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'b', 'c'], columns=['1st', '2nd', '3rd'])

frame3.drop(labels=['2nd'], axis=1)

frame3.drop(labels=['a', 'b'], axis=0, inplace=True)

frame3['a':'b']

temp_series = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
temp_series[[1, 2, 3]]

frame['1st']
frame[1:2]
frame.loc['a':'c', 'Ohio']

frame.get_value('a','Ohio')

df1 = pd.DataFrame(np.arange(12.0).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))

df2.loc[1, 'b'] = np.nan

df1 + df2

df1.add(df2, fill_value=1)

frame = pd.DataFrame(np.arange(12.0).reshape((4, 3)), columns=['b', 'd', 'e'], index=['Utah', 'Ohio', 'Texas', 'Oregon'])

# lambda
f = lambda x: x.max() - x.min()
f2 = lambda x, y: x + y

frame.apply(f, axis=0)
frame.apply(f, axis='columns')
frame.apply(f, axis=1)

def f3(x):
    return pd.Series([x.max(), x.min()], index=['max_value', 'min_value'])

format = lambda x: '%.2f' % x
format(0.2222222)

# sort
frame = pd.DataFrame({'a': [0, 1, 0, 1], 'b': [4, 7, -3, 2]}, index=['1st', '2nd', '3rd', '4st'])
frame.sort_values(by='a')

df = pd.DataFrame({'one':[1.4, 7.1, np.nan, 0.75], 'two':[np.nan, -4.5, np.nan, -1.3]}, index=['a', 'b', 'c', 'd'])
df.mean(axis='columns', skipna=False)
df.mean(axis='columns', skipna=True)

obj = pd.Series(['a', 'b', 'c', 'd'] * 4)
obj.describe()