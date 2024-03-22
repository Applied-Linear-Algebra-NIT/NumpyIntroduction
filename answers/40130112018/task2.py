# Your Implemetation
import numpy as np

one_d_array = np.array([1, 2, 3, 4, 5])
two_d_array = np.array([[1, 2, 3, 10], [4, 5, 6, 11], [7, 8, 9, 12]])
three_d_array = np.array(
    [
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
        [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]],
    ]
)

print(one_d_array[2])
print(two_d_array[2, 3])

sub_array = two_d_array[:2, :2]
print(sub_array)


for i in three_d_array:
    print(i)