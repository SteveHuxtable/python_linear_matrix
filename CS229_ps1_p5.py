import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read the training data and test data
df_tv = pd.read_csv('/Users/stevehu/Desktop/寒假书籍阅读/斯坦福CS229/stanford-cs229-master/Problem-set-1/data/quasar_train.csv')
cols_tv = df_tv.columns.values.astype(float).astype(int)
wave_lens = cols_tv

# read the test set
df_test = pd.read_csv('/Users/stevehu/Desktop/寒假书籍阅读/斯坦福CS229/stanford-cs229-master/Problem-set-1/data/quasar_test.csv')
cols_test = df_test.columns.values.astype(float).astype(int)

# to try to use local weighted regression fit the curvees for each data 
# tau = 5
# have a test on one piece of data
y = df_tv.loc[0]
X = np.stack([np.ones(cols_tv.shape), cols_tv]).T

theta_list = []

# design the function for local weighted linear regression
def weighted_optim(y, X, W):
    return np.linalg.inv(X.T.dot(W).dot(X)).dot(X.T).dot(W).dot(y)    

def get_weight_matrix(X, x_eval, tau=5):
    return np.diag(np.exp(-(X[:,1] - x_eval[1]) ** 2 / (2 * tau ** 2)))

# have a test on "get_weight_matrix()"
get_weight_matrix(X, X[:, 1], tau=5)

# plot the weighted regression curve
'''
preds = []
for k, x_eval in enumerate(X):
    W = get_weight_matrix(X, x_eval, tau=5)
    theta = weighted_optim(y, X, W)
    preds.append(theta.dot(x_eval))

preds = []
for x_eval in X:
    W = get_weight_matrix(X, x_eval, tau=5)
    theta = weighted_optim(y, X, W)
    preds.append(theta.dot(x_eval))

# plot the line chart of the data of the first line
plt.plot(wave_lens, df_tv.loc[1].values)
# plot the regression curve
plt.plot(wave_lens, preds) # seems all right
'''

# draw four figures with different tau
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.ravel()

for k, tau in enumerate([1, 10, 100, 1000]):
    ax = axes[k]
    preds = []
    for x_eval in X:
        W = get_weight_matrix(X, x_eval, tau=tau)
        theta = weighted_optim(y, X, W)
        preds.append(theta.dot(x_eval))

    ax.plot(wave_lens, df_tv.loc[0].values)
    ax.plot(wave_lens, preds)
    ax.set_title('tau = {0}'.format(tau))

# then, deal with the real spectrum data
def lwr_single(X, y, x, tau=tau):
    W = get_weight_matrix(X, x, tau=tau)
    theta = weighted_optim(X, y, W)
    return theta

def lwr(X, y, xs, tau):
    thetas = []
    for x in xs:
        th = lwr_single(X, y, x, tau)
        thetas.append(th)
    return thetas

# smoothed spectrum: training set
fs_tv = []
x0 = np.ones(df_tv.shape[1])
x1 = wave_lens
X= np.stack([x0, x1]).T
for k, row in df_tv.iterrows():
    print(k, end=",")
    y = row.values
    thetas = lwr(X, y, X, tau=5)
    prd = [_t.dot(_x) for (_t, _x) in zip(thetas, X)]
    fs_tv.append(prd)
df_fs_tv = pd.DataFrame(fs_tv, columns=df_tv.columns)

# smoothed spectrum: test set
fs_test = []
x0 = np.ones(df_test.shape[1])
x1 = wave_lens
X = np.stack([x0, x1]).T
# used for calculating distances d(f1, f2)
for k, row in df_test.iterrows():
    print(k, end=',')
    y = row.values
    thetas = lwr(X, y, X, tau=5)
    prd = [_t.dot(_x) for (_t, _x) in zip(thetas, X)]
    fs_test.append(prd)
df_fs_test = pd.DataFrame(fs_test, columns=df_test.columns)

# function regression
wl_right = wave_lens[wave_lens >= 1300]
wl_left = wave_lens[wave_lens < 1200]