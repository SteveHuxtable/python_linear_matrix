from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

''' emperical loss version 

try:
    xrange
except NameError:
    xrange = range

def add_intercept(X_):
    m, n = X_.shape
    X = np.zeros((m, n + 1))
    X[:, 0] = 1
    X[:, 1:] = X_
    return X

# load the data file
def load_data(filename):
    D = np.loadtxt(filename)
    Y = D[:, 0]
    X = D[:, 1:]
    return add_intercept(X), Y

def calc_grad(X, Y, theta):
    m, n = X.shape
    grad = np.zeros(theta.shape)

    margins = Y * X.dot(theta)
    probs = 1. / (1 + np.exp(margins))
    grad = -(1./m) * (X.T.dot(probs * Y))

    return grad

def logistic_regression(X, Y):
    m, n = X.shape
    theta = np.zeros(n)
    learning_rate = 10

    i = 0
    while True:
        i += 1
        prev_theta = theta
        grad = calc_grad(X, Y, theta)
        theta = theta  - learning_rate * (grad)
        norm = np.linalg.norm(prev_theta - theta)
        if i % 10000 == 0:
            print('Finished {0} iterations; Diff theta: {1}; theta: {2}; Grad: {3}'.format(
                i, norm, theta, grad))
        if norm < 1e-15:
            print('Converged in %d iterations' % i)
            break
    return

def main():
    print('==== Training model on data set A ====')
    Xa, Ya = load_data('data_a.txt')
    logistic_regression(Xa, Ya)

    print('\n==== Training model on data set B ====')
    Xb, Yb = load_data('data_b.txt')
    logistic_regression(Xb, Yb)

    return

if __name__ == '__main__':
    main()

'''

# the MLE and gradient regression version
# read the dataset and plot the distribution
dfb = pd.read_csv('data_b.txt', header=None, sep=' ', names=['label', 'x1', 'x2'])

'''
ax = plt.axes()
dfb.query('label == -1').plot.scatter(x='x1', y='x2', ax=ax, color='blue')
dfb.query('label == 1').plot.scatter(x='x1', y='x2', ax=ax, color='red')
'''

# then, we try to use MLE on the traing set to get the theta 
dfb.head()
list(dfb)
# get the dependent and independent variable
Yb = dfb[['label']].values
Yb = Yb.astype(int)
Xb = dfb[list(dfb)[1:]]
Yb[Yb == -1] = 0

# add the intercept columns
Xb = np.hstack([np.ones((Xb.shape[0], 1)), Xb.values])

def sigmoid(z):
    return (1 / 1 + np.exp(- z))

def deriv_sigmoid(z):
    return sigmoid(z) * (1 -sigmoid(z))

def logistic_p(theta, x, y):
    return ((sigmoid(theta.T.dot(x)) ** y) * (1 - sigmoid(theta.T.dot(x)) ** (1- y)) )

# have a test on the former 3 functions
test_xb = Xb[1].ravel()
test_theta = np.zeros(3)

test_xb.dot(test_theta)
Xb.dot(test_theta)

def log_regression(Y, X, alpha=5):
    # Y = Yb, X = Xb
    theta = np.zeros(X.shape[1])
