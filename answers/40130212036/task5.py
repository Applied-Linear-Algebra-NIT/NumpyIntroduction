import numpy as np

array = np.array([1, 2, 3, 4, 5])

mean = np.mean(array)
median = np.median(array)
variance = np.var(array)
std_deviation = np.std(array)

print("Descriptive Statistics:")
print("Mean:", mean)
print("Median:", median)
print("Variance:", variance)
print("Standard Deviation:", std_deviation)

# Correlation
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 4, 3, 2, 1])

correlation_coefficient = np.corrcoef(array1, array2)[0, 1]

print("\nCorrelation Coefficient between two arrays:")
print(correlation_coefficient)