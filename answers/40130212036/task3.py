import numpy as np

array1 = np.array([[1, 2, 3],
                   [4, 5, 6]])

array2 = np.array([[7, 8, 9],
                   [10, 11, 12]])

addition = array1 + array2
subtraction = array1 - array2
multiplication = array1 * array2
division = array1 / array2

print("Element-wise addition:")
print(addition)

print("\nElement-wise subtraction:")
print(subtraction)

print("\nElement-wise multiplication:")
print(multiplication)

print("\nElement-wise division:")
print(division)

# Broadcasting
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

vector = np.array([10, 20, 30])

result = matrix + vector[:, np.newaxis]
print("\nBroadcasting: Adding a vector to each column of a matrix:")
print(result)

# Reshaping and Flattening
three_dim_array = np.array([[[1, 2, 3],
                              [4, 5, 6]],
                             
                             [[7, 8, 9],
                              [10, 11, 12]],
                             
                             [[13, 14, 15],
                              [16, 17, 18]]])

# Reshape to a two-dimensional array
two_dim_array = three_dim_array.reshape(3, 6)
print("\nReshaped to a two-dimensional array:")
print(two_dim_array)

# Flatten to a one-dimensional array
one_dim_array = three_dim_array.flatten()
print("\nFlattened to a one-dimensional array:")
print(one_dim_array)