import numpy as np

# Creating a one-dimensional Python list:
pList = [1,2,3,4,5,6]

# Creating a Numpy array from the Python list:
npList = np.array(pList)

# Displaying the dimensions, shape, size,
# data type, and the sum of its elements:
print("One-dimensional array:")
print("Dimensions:", npList.ndim)
print("Shape:", npList.shape)
print("Size:", npList.size)
print("Data type:", npList.dtype)
print("Sum of elements:", np.sum(npList))
print("/----------------------------\\")

# -----------------------------------------------

# Creating a zero filled 3 by 4 matrix: 
threeByFourMatrix = np.zeros((3, 4))

# Displaying the dimensions, shape, size,
# data type, and the sum of its elements:
print("Zero-filled 3 by 4 matrix:")
print("Dimensions:", threeByFourMatrix.ndim)
print("Shape:", threeByFourMatrix.shape)
print("Size:", threeByFourMatrix.size)
print("Data type:", threeByFourMatrix.dtype)
print("Sum of elements:", np.sum(threeByFourMatrix))
print("/----------------------------\\")

# -----------------------------------------------

# Creating a 2 by 3 by 4 matrix filled with ones: 
# (threeDimensionalMatrix = tDM)
tDM =  np.ones((2,3,4))

# Displaying the dimensions, shape, size,
# data type, and the sum of its elements:
print("Three-dimensional array:")
print("Dimensions:", tDM.ndim)
print("Shape:", tDM.shape)
print("Size:", tDM.size)
print("Data type:", tDM.dtype)
print("Sum of elements:", np.sum(tDM))
print("/----------------------------\\")
