import numpy as np


arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])


# 1. Descriptive Statistics
# Mean
mean = np.mean(arr1)
print(f"The \"Mean\" is:\n{mean}\n")
# Median
median = np.median(arr1)
print(f"The \"Median\" is:\n{median}\n")
# Variance
variance = np.var(arr1)
print(f"The \"Variance\" is:\n{variance}\n")
# Standard Deviation 
std_dev = np.std(arr1)
print(f"The \"Standard Deviation\" is:\n{std_dev}\n")


# 2. Correlation
correlation = np.corrcoef(arr1, arr2)[0, 1]
print(f"The \"Correlation Coefficient\" between arr1 & arr2 is:\n{correlation}\n")
