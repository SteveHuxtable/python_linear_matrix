import numpy as np
import pandas as pd
from scipy import linalg

A = np.array([[2, 1],
              [1, 2]])

evalue, evector = linalg.eig(A)
evalue
evector