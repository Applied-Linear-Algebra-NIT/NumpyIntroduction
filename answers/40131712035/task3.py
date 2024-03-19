import numpy as np

# 1.Arithmetic Operations:
arr1 = np.array([2, 4, 6, 8])
arr2 = np.array([1, 2, 3, 4])

print("Element-wise Addition:", np.add(arr1, arr2))

print("Element-wise Subtraction:", np.subtract(arr1, arr2))

print("Element-wise Multiplication:", np.multiply(arr1, arr2))

print("Element-wise Division:", np.divide(arr1, arr2))

# 2.Broadcasting:
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
vector = np.array([[1], [2], [1], [2]])

print("Vector Added To Matrix Column-wise:\n", matrix + vector)

# 3.Reshaping and Flattening:
threeDArray = np.array([[[1, 1, 1], [2, 2, 2], [3, 3, 3]], [[4, 4, 4], [5, 5, 5], [6, 6, 6]]])
twoDArray = threeDArray.reshape(-1, threeDArray.shape[-1])
oneDArray = twoDArray.flatten()
print("3D Array:", threeDArray)
print("2D Array:", twoDArray)
print("1D Array:", oneDArray)
