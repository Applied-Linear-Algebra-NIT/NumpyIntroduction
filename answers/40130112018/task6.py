# Your Implemetation
import numpy as np
import matplotlib.pyplot as plt

x = np.array(range(100))
y = x ** 2

fitted = np.polyfit(x, y, 2)

print(fitted)

plt.plot(x, y)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Y = X^2")

plt.show()