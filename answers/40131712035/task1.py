import numpy as np

# 1.Array Creation:

oneDimensionalArray = np.array([1, 2, 3, 4])

twoDimensionalArray = np.zeros((3, 4))

threeDimensionalArray = np.ones((2, 3, 4))

# 2.Array Inspection:

print("1D Array:")
print(oneDimensionalArray.ndim)
print(oneDimensionalArray.shape)
print(oneDimensionalArray.size)
print(oneDimensionalArray.dtype)
print(oneDimensionalArray.sum())

print("\n2D Array:")
print(twoDimensionalArray.ndim)
print(twoDimensionalArray.shape)
print(twoDimensionalArray.size)
print(twoDimensionalArray.dtype)
print(twoDimensionalArray.sum())

print("\n3D Array:")
print(threeDimensionalArray.ndim)
print(threeDimensionalArray.shape)
print(threeDimensionalArray.size)
print(threeDimensionalArray.dtype)
print(threeDimensionalArray.sum())
