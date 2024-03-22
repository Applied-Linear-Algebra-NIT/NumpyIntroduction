import numpy as np

# first assignment

# ( 1-d array with 4 elements )
arr1 = np.array([1, 2, 3, 4])

# ( 2-d array filled with 0 )
zeros_arr2 = np.zeros((3, 4))

# ( 3-d array filled with 1 )
ones_arr3 = np.ones((2, 3, 4))

# second assignment

# arr1
dimensions_arr1 = np.ndim(arr1)
shape_arr1 = arr1.shape
size_arr1 = arr1.size
data_type_arr1 = arr1.dtype
sum_arr1 = arr1.sum()
print(
    '< arr1 >', '\n',
    'dimensions: ', dimensions_arr1, '\n',
    'shape: ', shape_arr1, '\n',
    'size: ', size_arr1, '\n',
    'data type: ', data_type_arr1, '\n',
    'sum: ', sum_arr1
)

print('\n---------------------------\n')

# zeros_arr2
dimensions_zeros_arr2 = np.ndim(zeros_arr2)
shape_zeros_arr2 = zeros_arr2.shape
size_zeros_arr2 = zeros_arr2.size
data_type_zeros_arr2 = zeros_arr2.dtype
sum_zeros_arr2 = zeros_arr2.sum()
print(
    '< zeros_arr2 >', '\n',
    'dimensions: ', dimensions_zeros_arr2, '\n',
    'shape: ', shape_zeros_arr2, '\n',
    'size: ', size_zeros_arr2, '\n',
    'data type: ', data_type_zeros_arr2, '\n',
    'sum: ', sum_zeros_arr2
)

print('\n---------------------------\n')

# ones_arr3
dimensions_ones_arr3 = np.ndim(ones_arr3)
shape_ones_arr3 = ones_arr3.shape
size_ones_arr3 = ones_arr3.size
data_type_ones_arr3 = ones_arr3.dtype
sum_ones_arr3 = ones_arr3.sum()
print(
    '< ones_arr3 >', '\n',
    'dimensions: ', dimensions_ones_arr3, '\n',
    'shape: ', shape_ones_arr3, '\n',
    'size: ', size_ones_arr3, '\n',
    'data type: ', data_type_ones_arr3, '\n',
    'sum: ', sum_ones_arr3
)
