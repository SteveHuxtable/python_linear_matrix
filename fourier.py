import pandas as pd
import numpy as np
from sympy import integrate, cos, sin
from sympy.abc import x

e = integrate(sin(x)*cos(x), (x, 0, 2*np.pi))
print(e.evalf())