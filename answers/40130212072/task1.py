import numpy as np

my_list = [1, 2, 3, 4, 5]
array1 = np.array(my_list)
print("Shape:", array1)
print("dimensions:", array1.ndim)
print("Array shape", array1.shape)
print("Size", array1.size)
print("Data Type", array1.dtype)
print("Sum", np.sum(array1))
print("\n")

# ----------------------------------------------

array2 = np.zeros((3, 4))
print("Shape:\n", array2)
print("dimensions:", array2.shape)
print("Size:", array2.size)
print("Data Type", array2.dtype)
print("Sum", np.sum(array2))
print("\n")

# -----------------------------------------------

array3 = np.ones((2, 3, 4))
print("dimensions:", array3.shape)
print("Shape:\n", array3)
print("Size:", array3.size)
print("Data Type", array3.dtype)
print("Sum", np.sum(array3))











































