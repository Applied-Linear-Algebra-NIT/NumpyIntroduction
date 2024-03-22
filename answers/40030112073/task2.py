import numpy as np

# Example arrays
one_dimensional_array = np.array([10, 20, 30, 40, 50])
two_dimensional_matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
three_dimensional_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

# Indexing
# Access the third element of the one-dimensional array
third_element = one_dimensional_array[2]
print(f"Third element of one-dimensional array: {third_element}")

# Access the element at position ([2, 3]) in the two-dimensional matrix
element_at_2_3 = two_dimensional_matrix[2, 3]
print(f"Element at position ([2, 3]) in two-dimensional matrix: {element_at_2_3}")

# Slicing
# Extract a (2x2) sub-matrix from the upper left corner of the two-dimensional matrix
sub_matrix = two_dimensional_matrix[:2, :2]
print("Extracted (2x2) sub-matrix from the upper left corner:")
print(sub_matrix)

# Iterating
# Iterate over the three-dimensional array, printing each two-dimensional section
print("Iterating over the three-dimensional array:")
for i, section in enumerate(three_dimensional_array):
    print(f"Section {i + 1}:")
    print(section)
