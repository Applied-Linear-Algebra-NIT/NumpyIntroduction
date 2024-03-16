import numpy as np
# /-----------------Descriptive Statistics-----------------\

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Calculating the mean
mean = np.mean(array)

# Calculating the median
median = np.median(array)

# Calculating the variance
variance = np.var(array)

# Calculating the standard deviation
standarDeviation = np.std(array)

# Print the results
print("Array:", array)
print("Mean:", mean)
print("Median:", median)
print("Variance:", variance)
print("Standard Deviation:", standarDeviation)

# /-----------------Correlation-----------------\

# Creating two arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 6, 7, 8, 9])

# Computing the correlation coefficient
correlation_coefficient = np.corrcoef(array1, array2)[0, 1]
print("/-----------------\\")
print("Array 1:", array1)
print("Array 2:", array2)
print("Correlation Coefficient:", correlation_coefficient)
