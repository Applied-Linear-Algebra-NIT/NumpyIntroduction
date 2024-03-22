import numpy as np

# Arithmetic Operations
# Define two arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Perform element-wise addition, subtraction, multiplication, and division
addition = array1 + array2
subtraction = array1 - array2
multiplication = array1 * array2
division = array1 / array2

# Broadcasting
# Define a matrix and a vector
matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([1, 1, 1])

# Add the vector to each column of the matrix (demonstrating broadcasting)
broadcasted_addition = matrix + vector

# Reshaping and Flattening
# Define a three-dimensional array
three_dim_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

# Reshape the three-dimensional array into a two-dimensional array
reshaped_array = three_dim_array.reshape(2, 6)

# Flatten the three-dimensional array into a one-dimensional array
flattened_array = three_dim_array.flatten()

# Output results
print("Arithmetic Operations:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

print("\nBroadcasting:")
print("Broadcasted Addition:\n", broadcasted_addition)

print("\nReshaping and Flattening:")
print("Reshaped Array:\n", reshaped_array)
print("Flattened Array:", flattened_array)
