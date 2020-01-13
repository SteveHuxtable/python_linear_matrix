path = 'usagov_bitly_data.txt'
# just read the first line in the dataset
test = open(path).readline()
print(test)

import json
path = 'usagov_bitly_data.txt'
records = [json.loads(line) for line in open(path)]
# print(records[0])

# time_zones = [rec['tz'] for rec in records]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print(time_zones[:10])

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

# counts = get_counts(time_zones)
# print(counts['America/New_York'])

# a better version of get_counts()
from collections import defaultdict

def get_counts2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts

def top_counts(count_dict, n = 10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

count_dic = get_counts2(time_zones)

print(top_counts(count_dic))

from collections import Counter
counts = Counter(time_zones)
counts.most_common(10)


import json
path = 'usagov_bitly_data.txt'
records = [json.loads(line) for line in open(path)]
# here we begin to use pandas
from pandas import DataFrame, Series
import pandas as pd 
import numpy as np
frame = DataFrame(records)
print(frame)
print(frame['tz'][:10])

tz_counts = frame['tz'].value_counts()
print(tz_counts[:10])

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
tz_counts[:10]

tz_counts[:10].plot(kind = 'barh', rot = 0)