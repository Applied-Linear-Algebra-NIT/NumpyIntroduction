import numpy as np
import matplotlib.pyplot as plt
#Polynomial Fitting
#points (x, y)
x = np.array([2, 1, 2, 8, 4, 6])
y = np.array([0.2, 0.8, 0.9, 1, -0.8, -1])
coefficients = np.polyfit(x, y, 2)
#Creating a polynomial function
poly= np.poly1d(coefficients)
#point for fitted curve
x_fit = np.linspace(min(x), max(x), 100)
y_fit = poly(x_fit)
#Plot the points and the fitted curve
plt.scatter(x, y, color='yellow', label='Data Points')
plt.plot(x_fit, y_fit, color='black', label='Fitted Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()

