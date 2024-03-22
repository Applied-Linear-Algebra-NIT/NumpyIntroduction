import numpy

arr1 = numpy.array([9, 5, 3, 13, 20])

arr2 = numpy.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

arr3 = numpy.array([[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
                    [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]])

# Display Array Dimensions
print("array 1 dimension: ", arr1.ndim)
print("array 2 dimension: ", arr2.ndim)
print("array 3 dimension: ", arr3.ndim)

# Display Array Shape
print("\narray 1 shape: ", arr1.shape)
print("array 2 shape: ", arr2.shape)
print("array 3 shape: ", arr3.shape)

# Display Array size
print('\narray 1 size:', arr1.size)
print('array 2 size:', arr2.size)
print('array 3 size:', arr3.size)

# Display Array Data type
print('\narray 1 data type: ', arr1.dtype)
print('array 2 data type: ', arr2.dtype)
print('array 3 data type: ', arr3.dtype)

# Display sum of array's element
print('\nsum of array 1 elements: ', numpy.sum(arr1))
print('sum of array 2 elements: ', numpy.sum(arr2))
print('sum of array 3 elements: ', numpy.sum(arr3))






