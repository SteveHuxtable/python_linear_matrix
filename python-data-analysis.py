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