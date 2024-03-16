import numpy as np
# /-----------------Arithmetic Operations-----------------\

# Creating two arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Element-wise addition
addition_result = array1 + array2

# Element-wise subtraction
subtraction_result = array1 - array2

# Element-wise multiplication
multiplication_result = array1 * array2

# Element-wise division
# Note: Division by zero will result in a warning, but the operation will proceed, filling the corresponding result element with 'inf' (infinity) or 'nan' (not a number).
division_result = array1 / array2

print("Array 1:")
print(array1)
print("\nArray 2:")
print(array2)
print("\nElement-wise addition:")
print(addition_result)
print("\nElement-wise subtraction:")
print(subtraction_result)
print("\nElement-wise multiplication:")
print(multiplication_result)
print("\nElement-wise division:")
print(division_result)
print("\n/-----------------\\")

# /-----------------Broadcasting-----------------\

# Creating a matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Creating a vector to add to each column
vector = np.array([10, 20, 30])

# Adding the vector to each column of the matrix using broadcasting
result = matrix + vector

print("Original Matrix:")
print(matrix)
print("\nVector:")
print(vector)
print("\nResult after broadcasting:")
print(result)
print("\n/-----------------\\")

# /-----------------Reshaping and Flattening-----------------\

# Three-dimensional matrix:
tDM = np.ones((2, 3, 4))

# The general syntax of the reshape() function is:
#           numpy_array.reshape(new_shape)
# new_shape is the desired new shape specified as a tuple of integers.

# One of the dimensions in the new shape can be -1, which means it will be
# automatically calculated based on the size of the array and the other dimensions.
twoD = tDM.reshape(-1, 4)

# Flatten the two-dimensional array into a one-dimensional array
oneD = twoD.flatten()

print("The original array: \n\n", tDM)
print("The reshaped array: \n\n", twoD)
print("The flatten array: \n\n", oneD)

# Note that the number of the elements should be the same
