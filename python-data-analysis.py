# for chapter 10
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# create the df
df = pd.DataFrame({'data1': np.random.randn(5),
                   'data2': np.random.randn(5),
                   'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one']})

dict(list(df.groupby('key1')))

for name, group in df.groupby('key1'):
    print(name)
    print(group)

df.dtypes

# data aggregation
df = pd.DataFrame({'data1': np.random.randn(5),
                   'data2': np.random.randn(5),
                   'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one']})

grouped = df.groupby('key1')
grouped['data1'].quantile(0.9)
grouped_data1 = grouped['data1']
grouped_data1.quantile(0.9)
grouped_data1.mean()
grouped_data1.agg('mean')
grouped_data1.agg('sum')

def peak_to_peak(arr):
    return arr.max() - arr.min()

grouped.agg(peak_to_peak)
grouped.quantile(0.9)
grouped.describe()

tips = pd.read_csv('tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']
grouped = tips.groupby(['day', 'smoker'])

grouped_pct = grouped['tip_pct']
grouped_pct.mean()

# fill data with na value
s = pd.Series(np.random.randn(6))
s[::2] = np.nan
s.fillna(s.mean())

df = pd.DataFrame({'category': ['a', 'a', 'a', 'a',
                                'b', 'b', 'b', 'b'],
                                'data': np.random.randn(8),
                                'weights': np.random.randn(8)})

grouped = df.groupby('category')
get_wavg = lambda g: np.average(g['data'], weights=g['weights'])
grouped.apply(get_wavg)

close_px = pd.read_csv('stock_px_2.csv', parse_dates=True, index_col=0)
close_px.info()
close_px.corrwith(close_px['SPX']) # to calculate the correlation

spx_corr = lambda x: x.corrwith(x['SPX'])

tips = pd.read_csv('tips.csv')
tips.pivot_table(index=['day', 'smoker'])

grouped = tips.groupby(['day', 'smoker'])
grouped.mean()