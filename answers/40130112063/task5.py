import numpy as np

array_1 = np.array([1, 2, 3, 4, 5])
array_2 = np.array([5, 4, 3, 2, 1])

# Descriptive Statistics

print("Array 1:\n", array_1)

mean_value = np.mean(array_1)
print("Mean of array 1 is:", mean_value)

median_value = np.median(array_1)
print("Median of array 1:", median_value)

variance = np.var(array_1)
print("Variance of array 1:", variance)

std_value = np.std(array_1)
print(f"Standard deviation of array 1: {std_value}")

# Correlation
correlation_coefficient = np.corrcoef(array_1, array_2)
print(f"Correlation between array 1 and array 3 : {correlation_coefficient}")
