import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

# one-dimentional vector and its transpose
A = np.array([1, 2, 3, 4])
A_t = A[:, np.newaxis]
A.dot(A_t)
print(A.T)

# two-dimentional
A = np.array([[1, 2, 3, 4]])
A.T
A.dot(A.T).ravel()
# same as 
np.dot(A, A.T)

# dot product
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.dot(a, b)

# not okay!
a = np.array([[1, 2, 3]])
b = np.array([[3, 4, 5]])
np.dot(a, b)

# a right version
np.dot(a, b.T)

# outer product
a = np.array([[3, 3, 9]])
b = np.array([[1, 4, 12]])
np.cross(a, b)

# try a Ax
A = pd.DataFrame(np.arange(3 * 3).reshape((3, 3)))
x = np.arange(3)
np.dot(A, x)
np.dot(A, x.T)
A.dot(x)
A.dot(x.T)

A = np.arange(9).reshape((3, 3))
A.shape
A.shape[0] # A.shape[1]

np.ones([5, 3])
np.ones((5, 3))
np.zeros((5, 3))
np.diag((1, 2, 3, 4, 5))
np.eye(10)

