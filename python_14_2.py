import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.display.max_rows = 10

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('users.dat', sep="::", header=None, columns=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ratings.dat', sep="::", header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('movies.dat', sep="::", header=None, names=mnames)

data = pd.merge(pd.merge(ratings, users), movies)

mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
ratings_by_title = data.groupby('title').size()
active_tiles = ratings_by_title.index[ratings_by_title >= 250]

# 14.3

