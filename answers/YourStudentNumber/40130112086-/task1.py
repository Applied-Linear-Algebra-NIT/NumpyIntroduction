import numpy as np
#task1.1

#Creating Python list
task1_list = [2,4,6,8]
#Creating NumPy array
task1_array = np.array(task1_list)
print("one-dimensional array")
print("Array:",task1_array)
print("Dimensions:",task1_array.ndim)
print("Shape:",task1_array.shape)
print("Size:",np.size(task1_array))
print("Data type:",task1_array.dtype)
print("Sum of elements:",np.sum(task1_array))

#task1.2

#creating 3*4 matrix
task1_matrix=np.zeros((3,4))
print("\nTwo-dimensional matrix")
print("Array:",task1_matrix)
print("Dimensions:",task1_matrix.ndim)
print("Shape:",task1_matrix.shape)
print("Size:",task1_matrix.size)
print("Data type:",task1_matrix.dtype)
print("Sum of elements:",np.sum(task1_matrix))

#task1.3

#creating 2*3*4 matrix
matrix=np.ones((2,3,4))
print("\nThree-dimensional array")
print("Array:",matrix)
print("Dimensions:",matrix.ndim)
print("Shape:",matrix.shape)
print("Size:",matrix.size)
print("Data type:",matrix.dtype)
print("Sum of elements:",np.sum(matrix))