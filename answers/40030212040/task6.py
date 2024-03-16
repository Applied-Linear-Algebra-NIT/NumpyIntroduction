import numpy as np
import matplotlib.pyplot as plt

# Original data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 6, 8])

# Fit a polynomial of degree 2
coefficients = np.polyfit(x, y, 2)
polyFunction = np.poly1d(coefficients)

# Generate x values for the fitted curve
x_fit = np.linspace(np.min(x), np.max(x), 100)
y_fit = polyFunction(x_fit)

# Plot the original data points
plt.scatter(x, y, label='Original Data Points')

# Plot the fitted curve
plt.plot(x_fit, y_fit, color='red', label='Fitted Curve')

# Adding labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Fitting')
plt.legend()

# Showing the plot
plt.grid(True)
plt.show()
