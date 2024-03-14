import numpy as np

arr = np.array([1, 2, 3, 4, 5])
median = np.median(arr)
mean = np.mean(arr)
variance = np.var(arr)
std_deviation = np.std(arr)

print("arr:", arr)
print("median:", median)
print("mean:", mean)
print("variance:", variance)
print("std_deviation:", std_deviation)

# ---------------------------------------------

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 4, 3, 2, 1])

corr = np.corrcoef(array1, array2)[0, 1]
print("corr: ", corr)
