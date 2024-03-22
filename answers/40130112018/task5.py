# Your Implemetation
import numpy as np

a = np.array([1, 2, 3, 4, 5])

print(np.mean(a))
print(np.median(a))
print(np.var(a))
print(np.std(a))

b = np.array([6, 7, 8, 9, 10])

corr_coef = np.corrcoef(a, b)

print(corr_coef)