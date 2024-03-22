import matplotlib.pyplot as plt
import numpy as np

arr1 = np.array([1, 2, 12, 9])
arr2 = np.array([3, 6, 9, 12])

poly_with_deg2 = np.polyfit(arr1, arr2, deg=2)

polynomial = np.poly1d(poly_with_deg2)

fitted_arr1 = np.linspace(min(arr1), max(arr1), 50)
fitted_arr2 = polynomial(fitted_arr1)

plt.scatter(arr1, arr2, color='darkred')
plt.plot(fitted_arr1, fitted_arr2, color='darkblue')

plt.show()
