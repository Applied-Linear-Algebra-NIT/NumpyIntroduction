import numpy as np

one_dim_array = np.array([1, 2, 3, 4, 5])

two_dim_matrix = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]])

three_dim_array = np.array([[[1, 2, 3],
                              [4, 5, 6]],
                             
                             [[7, 8, 9],
                              [10, 11, 12]],
                             
                             [[13, 14, 15],
                              [16, 17, 18]]])

# Indexing
third_element = one_dim_array[2]
element_2_3 = two_dim_matrix[1, 2]
print("Third element of the one-dimensional array:", third_element)
print("Element at position (2, 3) in the two-dimensional matrix:", element_2_3)

# Slicing
sub_matrix = two_dim_matrix[:2, :2]
print("Sub-matrix from the upper left corner of the two-dimensional matrix:\n", sub_matrix)

# Iterating
print("Iterating over the three-dimensional array:")
for matrix in three_dim_array:
    print(matrix)