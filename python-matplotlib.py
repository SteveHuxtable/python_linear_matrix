import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax2.plot(np.random.randn(50).cumsum(), 'g--')
plt.show()

fig2, axes = plt.subplots(2, 3)
axes[1, 1].plot(np.random.randn(10).cumsum(), linestyle='--', color='r')
fig2.show()

# draw a plot with necessary elements
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(100).cumsum(), 'k--', label='Default')
ax.plot(np.random.randn(100).cumsum(), 'r-', label='Second line')
fig.legend(loc='best')

fig.show()

# plot with manual annote
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

df = pd.read_csv('spx.csv', index_col=0, parse_dates=True)
spx = df['SPX']

spx.plot(ax=ax, style='k-')
# df.plot(ax=ax, style='k-')
ax.set_xlim(['1/1/2007', '1/1/2011'])
ax.set_ylim([600, 1800])
ax.set_title('Financial crisis: 2008 - 2010')

fig.show()

s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
s.plot()
plt.show()
plt.close()

# do a homework
fig, ax = plt.subplots(2, 1)

data = pd.Series(np.random.randn(16), index=list('abcdefghijklmnop'))
data.plot.bar(ax=ax[0], color='k', alpha=0.7)
data.plot.barh(ax=ax[1], color='r', alpha=0.7)

plt.show()
plt.close()

# clustered bar figure:w

tips = pd.read_csv('tips.csv')
party_counts = pd.crosstab(tips['day'], tips['size'])
party_counts.head()
party_counts = party_counts.loc[:, 2:5]

party_counts = party_counts.div(party_counts.sum(1), axis=0)
party_counts.plot.bar()

plt.show()
plt.close()

# use seaborn
tips.head()
