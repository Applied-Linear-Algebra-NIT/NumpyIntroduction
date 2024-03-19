import numpy as np


oneD_array = np.array([1, 2, 3, 4, 5])
twoD_zero_array = np.zeros((3, 4))
threeD_one_array = np.ones((2, 3, 4))

# 1. Indexing
# the third element of the one-dimensional array
print(f"The third element of the one-dimensional array:\n{oneD_array[2]}\n")
# the element at position ([2, 3]) in the two-dimensional matrix
print(f"The element at position ([2, 3]) in the two-dimensional matrix:\n{twoD_zero_array[2, 3]}\n")


# 2. Slicing
print(f"The (2 times 2) sub-matrix from the upper left corner of the two-dimensional matrix:\n{twoD_zero_array[:2, :2]}\n")


# 3. Iterating
print("Printing each two-dimensional section, in the three-dimensional array:")
for twoD_arr in threeD_one_array:
    print(f"{twoD_arr}\n")
