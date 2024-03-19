import numpy as np

# 1.Descriptive Statistics:
array1 = np.array([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10])
print("Mean:", np.mean(array1))
print("Median:", np.median(array1))
print("Variance:", np.var(array1))
print("Standard Deviation:", np.std(array1))

# 2.Correlation:
array2 = np.array([1, 1, 4, 5, 7, 9, 45, 22, 12, 0, 88])
print("\nCorrelation Coefficient:", np.corrcoef(array1, array2))
