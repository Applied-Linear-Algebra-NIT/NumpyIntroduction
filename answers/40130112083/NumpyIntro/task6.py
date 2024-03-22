import numpy as np

a = np.array([1.5, 10.3, 11, 5])
b = np.array([4, 13, 2, 6.8])
c = np.polyfit(a, b, 2)
print(c)

