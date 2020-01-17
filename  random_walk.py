import random
import numpy as np

position = 0  
walk = [position]
steps = 1000

for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

print(walk)

# then we can draw a plot for this