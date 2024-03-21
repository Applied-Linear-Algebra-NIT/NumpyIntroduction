import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

coefficients = np.polyfit(x, y, 2)
poly_function = np.poly1d(coefficients)

x_fit = np.linspace(min(x), max(x), 100)
y_fit = poly_function(x_fit)

plt.scatter(x, y, label='Original Data Points')
plt.plot(x_fit, y_fit, color='red', label='Fitted Curve (Degree 2)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Fitting')
plt.legend()
plt.grid(True)
plt.show()