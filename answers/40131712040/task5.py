import numpy as np

arr = np.array([1, 2, 3, 4, 5])

median = np.median(arr)

avg = np.mean(arr)

variance = np.var(arr)

std_deviation = np.std(arr)

print("array:", arr)
print("median:", median)
print("avg:", avg)
print("variance:", variance)
print(" std_deviation:", std_deviation)

print("--------------------------------------------------")

array1 = np.array([11, 22, 33, 44, 55])
array2 = np.array([55, 44, 33, 22, 11])

corr = np.corrcoef(array1, array2)[0, 1]
print("corr of two array: ", corr)


