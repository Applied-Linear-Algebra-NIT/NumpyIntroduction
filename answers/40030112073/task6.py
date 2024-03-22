import numpy as np
import matplotlib.pyplot as plt

# Given data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

# Fit a polynomial of degree 2
coefficients = np.polyfit(x, y, 2)

# Generate a polynomial function from the coefficients
polynomial = np.poly1d(coefficients)

# Generate x values for the fitted curve
x_fitted = np.linspace(x[0], x[-1], 100)

# Generate y values for the fitted curve
y_fitted = polynomial(x_fitted)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Original data points')
plt.plot(x_fitted, y_fitted, '-', label='Fitted polynomial curve')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Fitting')
plt.grid(True)
plt.show()
