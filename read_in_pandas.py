import pandas as pd
from pandas import Series, DataFrame
import numpy as np

pd.options.display.max_rows = 10

df = pd.read_csv('examples/ex1.csv', header=None)

df2 = pd.read_csv('examples/ex1.csv', index_col='message')

# read some lines in df
hundred_lines = pd.read_csv('examples/ex6.csv', nrows=100)
hundred_lines['key']
hundred_lines['key'].value_counts()

# read data by iteration
chunker = pd.read_csv('examples/ex6.csv', chunksize=500)
tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
tot = tot.sort_values(ascending=False)

dates = pd.date_range('1/1/2000', periods=365)
df = Series(np.arange(365), index=dates)

df.to_csv('examples/test_1.csv')

import csv
f = open('examples/ex7.csv')
reader = csv.reader(f)

for line in reader:
    print(line)

with open('examples/ex7.csv') as f:
    lines = list(csv.reader(f))

header, values = lines[0], lines[1:]

data_dict = {h: v for h, v in zip(header, zip(*values))}
# have a test on the zip()
test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

import json

siblings = pd.DataFrame([['Scott', '30'], ['Katie', '38']], index=[0, 1], columns=['name', 'age'])

print(siblings.to_json())