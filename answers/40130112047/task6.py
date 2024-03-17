import numpy as np
import matplotlib.pyplot as plt

# Generate some example data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.3, 3.4, 4.1, 4.8, 6.0])     # y values

# Fit the data of degree 2
coefficients = np.polyfit(x, y, 2)
p = np.poly1d(coefficients)     # create polynomial
print("p : ", p)

# Generate 100 points along the curve for the fitted polynomial
# between x[0] and last x element
x_fit = np.linspace(x[0], x[-1], 100)
print("x-fit : ", x_fit)
y_fit = p(x_fit)
print("y-fit : ", y_fit)

# Plot the original data points and the fitted curve
plt.figure()
plt.scatter(x, y, color='blue', label='Original Data Points')  # draws points
plt.plot(x_fit, y_fit, color='red', label='Fitted Curve (Degree 2)')   # draws curve
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fitting a Quadratic Polynomial')
plt.legend()
plt.grid(True)
plt.show()