import numpy as np
import matplotlib.pyplot as plt

x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([2, 3, 5, 8, 10])

# Fit a polynomial of degree 2
coefficients = np.polyfit(x_data, y_data, 2)
p = np.poly1d(coefficients)

# Generate x values for plotting
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = p(x_fit)

# Plot the original data points
plt.scatter(x_data, y_data, label="Data Points", color="blue")

# Plot the fitted curve
plt.plot(x_fit, y_fit, label="Fitted Curve", color="red")

# Add labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Polynomial Fitting (Degree 2)")

# Add legend
plt.legend()

plt.show()
