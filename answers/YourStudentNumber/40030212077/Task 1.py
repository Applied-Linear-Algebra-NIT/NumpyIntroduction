import numpy as np

def array_info(array):

    # array
    print(f"array:\n{array}")

    # dimensions
    print(f"\ndimensions:\n{array.ndim}")
    
    # shape
    print(f"\nshape:\n{array.shape}")
    
    # size
    print(f"\nsize:\n{array.size}")
    
    # data type
    print(f"\ndata type:\n{array.dtype}")
    
    # sum of elements
    print(f"\nsum of elements:\n{np.sum(array)}\n")

# 1. Array Creation
oneD_array = np.array([1, 2, 3, 4, 5])
twoD_zero_array = np.zeros((3, 4))
threeD_one_array = np.ones((2, 3, 4))

# 2. Array Inspection
array_info(oneD_array)
array_info(twoD_zero_array)
array_info(threeD_one_array)
