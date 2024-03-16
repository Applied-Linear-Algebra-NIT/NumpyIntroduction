import numpy as np

x = np.array([1.0,2.0,3.0,4.0])
y = np.array([0.5,0.8,1.2,0.8])
z = np.polyfit(x, y, 2)
print(z)
