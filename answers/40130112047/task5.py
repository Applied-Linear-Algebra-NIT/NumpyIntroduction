import numpy as np

arr = np.array([[9, 8, 7],
                [6, 5, 4],
                [3, 2, 1]])

print("Matrix :\n", arr)
print("Mean of matirx :\n", np.mean(arr))
print("Median of matirx :\n", np.median(arr))
print("Variance of matirx :\n", np.var(arr))
print("Standard devision of matirx :\n", np.std(arr))

print("-"*40,"\n")


array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([1, 2, 3, 4, 5])

correlation_coefficient = np.corrcoef(array1, array2)[0, 1]

# The resulting correlation coefficient value ranges from -1 to 1, where:
#1 indicates a perfect positive linear relationship,
#-1 indicates a perfect negative linear relationship,
#0 indicates no linear relationship.

print("Array 1:", array1)
print("Array 2:", array2)
print("Correlation Coefficient:", correlation_coefficient)