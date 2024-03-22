import numpy as np

############# TASK 1 #############
one_d_array = np.array([1, 2, 3, 4, 5])

print(one_d_array)

# 3 by 4 array
two_d_array = np.array([[1, 2, 3, 10], [4, 5, 6, 11], [7, 8, 9, 12]])

print(two_d_array)


# 2 by 3 by 4 array

three_d_array = np.array(
    [
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
        [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]],
    ]
)

print(three_d_array)
