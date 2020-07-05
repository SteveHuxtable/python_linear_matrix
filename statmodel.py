import pandas as pd
import numpy as np
import patsy

data = pd.DataFrame({'x0': [1, 2, 3, 4, 5],
                     'x1': [0.01, -0.01, 0.25, -4.10, 0.00],
                     'y': [-1.5, 0.0, 3.6, 1.3, -2.0]})
                     
df2 = pd.DataFrame(data.values, columns=['one', 'two', 'three'])

df3 = data.copy()
df3['strings'] = ['a', 'b', 'c', 'd', 'e']

data['category'] = pd.Categorical(['a', 'b', 'a', 'a', 'b'], categories=['a', 'b'])
dummies = pd.get_dummies(data.category, prefix='category')
data_with_dummies = data.drop('category', axis=1).join(dummies)

y, X = patsy.dmatrices('y ~ x0 + x1', data)
# y, X = patsy.dmatrices('y ~ x0 + x1 + 0', data)

coef, resid, nani, nani2 = np.linalg.lstsq(X, y)
coef = pd.Series(coef.squeeze(), index=X.design_info.column_names)

data = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a', 'b', 'a', 'b'],
                     'key2': [0, 1, 0, 1, 0, 1, 0, 0],
                     'v1': [1, 2, 3, 4, 5, 6, 7, 8],
                     'v2': [-1, 0, 2.5, -0.5, 4.0, -1.2, 0.2, -1.7]})

y, X = patsy.dmatrices('v2 ~ key1', data)
y, X = patsy.dmatrices('v2 ~ key1 + 0', data)

import statsmodels.api as sm
import statsmodels.formula.api as smf

def dnorm(mean, variance, size=1):
    if isinstance(size, int):
        size = size,
    return mean + np.sqrt(variance) * np.random.randn(*size)

np.random.seed(12345)
N = 100
dnorm(0, 0.2, size=N)
np.c_[dnorm(0, 0.2, size=N)]