import numpy as np

arr1d = np.array([1, 2, 3, 4, 5])
element1 = arr1d[2]

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
element2 = matrix[1, 2]

print("the third element of the one-dimensional array:", element1)
print("element at position ([2, 3]) in the two-dimensional matrix:", element2)

# -----------------------------------------------

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

sub_matrix = matrix[:2, :2]

print(sub_matrix)

# ------------------------------------------------

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for i in range(arr.shape[0]):
    print(arr[i])
    print()