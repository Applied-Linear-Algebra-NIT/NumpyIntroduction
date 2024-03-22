import numpy as np

arr1 = np.array([9, 5, 3, 13, 20])
arr2 = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
arr3 = np.array([[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
                    [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]])


print("Third element of array 1: ", arr1[2])
print("Element at position ([2, 3]) in array 2: ", arr2[2][3])

print('(2 times 2) sub-matrix from the upper left corner of array 2: ', arr2[0:2, 0:2])

# Iterating
for x in arr3:
    print('\n2-D section:')
    print(x)
