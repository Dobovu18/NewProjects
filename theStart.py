import numpy as np
import matplotlib.pyplot as plt
import math

def indicator(x, a, b):
    if a < x < b:
        return 1
    else:
        return 0

x = np.linspace(-math.pi, math.pi, 100)
y = np.sin(x) #indicator(x, -1, 1)

plt.plot(x, y)
plt.show()