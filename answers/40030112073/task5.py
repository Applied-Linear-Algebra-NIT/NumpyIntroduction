import numpy as np

# Descriptive Statistics
data_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

mean = np.mean(data_array)
median = np.median(data_array)
variance = np.var(data_array)
standard_deviation = np.std(data_array)

# Correlation
array_x = np.array([1, 2, 3, 4, 5])
array_y = np.array([5, 4, 3, 2, 1])

correlation_coefficient = np.corrcoef(array_x, array_y)[0, 1]

# Results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {standard_deviation}")
print(f"Correlation Coefficient between array_x and array_y: {correlation_coefficient}")
