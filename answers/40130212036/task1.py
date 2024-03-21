import numpy as np

arr1d = np.array([1, 2, 3, 4, 5])

arr2d_zeros = np.zeros((3, 4))

arr3d_ones = np.ones((2, 3, 4))

def display_array_info(arr, name):
    print(f"Array Name: {name}")
    print(f"Dimensions: {arr.ndim}")
    print(f"Shape: {arr.shape}")
    print(f"Size: {arr.size}")
    print(f"Data Type: {arr.dtype}")
    print(f"Sum of Elements: {np.sum(arr)}")
    print()

display_array_info(arr1d, "arr1d")
display_array_info(arr2d_zeros, "arr2d_zeros")
display_array_info(arr3d_ones, "arr3d_ones")