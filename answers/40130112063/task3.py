import numpy as np

arr1 = np.array([[8, 1, 8], [3, 2, 0], [4, 4, 9]])
arr2 = np.array([[2, 4, 6], [1, 2, 7], [6, 9, 7]])
arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr4 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                 [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                 [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])
vec1 = np.array([[10], [20], [30]])

print('Array 1 :\n', arr1)
print('Array 2 :\n', arr2)

add_result = np.add(arr1, arr2)
print("Array 1 + Array 2:\n", add_result)

sub_result = np.subtract(arr1, arr2)
print("Array 1 - Array 2:\n", sub_result)

mul_result = np.matmul(arr1, arr2)
print("Array 1 * Array 2:\n", mul_result)

div_result = np.divide(arr1, arr2)
print("Array 1 / Array 2:\n", div_result)

# Broadcasting
print("Array 3 + vector 1:\n", np.add(arr3, vec1))

# Reshaping and Flattening
arr_2d = arr4.reshape(9,3)
print("Reshape 3D array to 2D array:\n", arr_2d)
arr_1d = arr4.flatten()
print("Flattening 3D array:\n", arr_1d)
