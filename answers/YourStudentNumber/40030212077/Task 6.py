import numpy as np
import matplotlib.pyplot as plt


# 1. Polynomial Fitting

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([2.1, 7.7, 13.6, 27.2, 40.9, 61.1])

coefficients = np.polyfit(x, y, 2)

polynomial = np.poly1d(coefficients)

x_curve = np.linspace(0, 5, 100)
y_curve = polynomial(x_curve)

error = np.sum((polynomial(x) - y) ** 2)

# Display
plt.scatter(x, y, label='Input')
plt.plot(x_curve, y_curve, color='red', label='Polynomial curve')
plt.title('Polynomial matching with input data')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.text(3, 40, f'Squared error: {error:.2f}')
plt.grid(True)
plt.show()
