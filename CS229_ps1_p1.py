import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %matplotlib inline # this is for jupyterNotebook

df_X = pd.read_csv('/Users/stevehu/Desktop/寒假书籍阅读/斯坦福CS229/stanford-cs229-master/Problem-set-1/data/logistic_x.txt', sep='\ +', header=None, engine='python')
ys = pd.read_csv('/Users/stevehu/Desktop/寒假书籍阅读/斯坦福CS229/stanford-cs229-master/Problem-set-1/data/logistic_y.txt', sep='\ +', header= None, engine='python')
ys = ys.astype(int)

df_X['label'] = ys[0].values

ax = plt.axes()

df_X.query('label == -1').plot.scatter(x=0, y=1, ax=ax, color='blue')
df_X.query('label == 1').plot.scatter(x=0, y=1, ax=ax, color='red')

'''
plt.scatter(x=df_X.query('label == 1')[0], y=df_X.query('label == 1')[1], color='blue')
'''

Xs = df_X[[0, 1]].values

# add a col of ones for the intercept terms, and also use column vectors
Xs = np.hstack([np.ones((Xs.shape[0], 1)), Xs])
ys = df_X['label'].values

all_thetas = [] # collect for demonstrate purpose
theta = np.zeros(Xs.shape[1])

tol = 1e9
n_iters = 0

while tol > 1e-6:
    zs = ys * Xs.dot(theta)
    gzs = 1 / (1 + np.exp(-zs))
    nabla = np.mean((gzs - 1) * ys * Xs.T, axis=1)

    # Refactor, more efficient way of calculating hessian
    hessian = np.zeros((Xs.shape[1], Xs.shape[1]))
    for i in range(hessian.shape[0]):
        for j in range(hessian.shape[0]):
            if i <= j:
                hessian[i][j] = np.mean(gzs * (1 - gzs) * Xs[:,i] * Xs[:,j])
                if i != j:
                    hessian[j][i] = hessian[i][j]

    delta = np.linalg.inv(hessian).dot(nabla)
    old_theta = theta.copy()
    theta -= delta
    all_thetas.append(theta.copy())
    n_iters += 1
    tol = np.sum(np.abs(theta - old_theta))

print('converged after {0} iterations'.format(n_iters))