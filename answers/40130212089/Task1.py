import numpy as np
# Part 1
array1D = np.array([0, 1, 2, 3, 4])
array2D = np.zeros((3, 4))
array3D = np.ones((2, 3, 4))
print('Task 1:')
# Part 2
print(f'1D array: \n{array1D}\nDimensions: {array1D.ndim}\nShape: {array1D.shape}\nSize: {array1D.size}\nData Type: {array1D.dtype}\nSum of all array elements: {np.sum(array1D)}')
print(f'1D array: \n{array2D}\nDimensions: {array2D.ndim}\nShape: {array2D.shape}\nSize: {array2D.size}\nData Type: {array2D.dtype}\nSum of all array elements: {np.sum(array2D)}')
print(f'1D array: \n{array3D}\nDimensions: {array3D.ndim}\nShape: {array3D.shape}\nSize: {array3D.size}\nData Type: {array3D.dtype}\nSum of all array elements: {np.sum(array3D)}')