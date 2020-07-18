import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mglearn

x, y = mglearn.datasets.make_forge()
x = pd.DataFrame(x, columns=['First feature', 'Second feature'])
df = x.copy()
df['Class'] = y

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

df_group0 = df[df.Class == 0]
df_group1 = df[df.Class == 1]

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
type(cancer)
cancer.keys()