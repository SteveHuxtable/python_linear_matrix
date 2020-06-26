import numpy as np
import pandas as pd
from numpy import nan as NA

test_series = pd.Series(['a', 'b', 'c', NA, 'd'], index=[1, 2, 3, 4, 5])
test_series.dropna()
test_series

df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = NA
df.iloc[4:, 2] = NA

# fill the na with mean(col)
df.fillna({1: df.mean()[1], 2: df.mean()[2]})

# review python apply
test_map_df = pd.DataFrame({'a': [1, 2, 3, 1, 2, 3], 'b': [1, 1, 1, 2, 2, 2]})
temp_map = {1: '1st', 2: '2nd', 3: '3rd'}
test_map_df['turn'] = test_map_df['a'].map(temp_map)

# add 1 on the first col
test_map_df['a'].map(lambda x: x + 1)

# cut the data using pd.cut()
test_series = np.random.rand(40)
test_cut = pd.cut(test_series, bins = 3, precision=3)

np.random.seed(1234)
values = np.random.rand(10)

bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
pd.cut(values, bins)

pd.get_dummies(pd.cut(values, bins))

# read a dat file
movies = pd.read_table('movies.dat', sep='::', header=None, names=['movie_id', 'title', 'genres'])

all_genres = []

for x in movies.genres:
    all_genres.extend(x.split('|'))

all_genres = pd.unique(all_genres)