import numpy as np
import matplotlib.pyplot as plt
# Polynomial Fitting:
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 3, 5])

# Fit a second-degree polynomial to the data
coefficients = np.polyfit(x, y, 2)

# Create a polynomial function with the fitted coefficients
polynomial = np.poly1d(coefficients)

# Generate a range of x-values for plotting the fitted curve
x_fit = np.linspace(min(x), max(x), 100)

# Evaluate the polynomial at each x-value
y_fit = polynomial(x_fit)

# Plot the original data points
plt.scatter(x, y, label='Original Data')

# Plot the fitted curve
plt.plot(x_fit, y_fit, label='Fitted Curve', color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()
