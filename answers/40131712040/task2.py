import numpy as np

array_1D = np.array([10, 20, 30, 40, 50])
element_at_index_2 = array_1D[2]
array_2D = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

element_at_2_3 = array_2D[1, 2]

print("third element in array_1D :", element_at_index_2)
print("element at position [3,2] in array_2D:", element_at_2_3)

print("---------------------------------------------------")

matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

sub_of_matrix = matrix[:2, :2]
print(sub_of_matrix)

print("---------------------------------------------------")

Array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for i in range(Array.shape[0]):
    print(f'Two_dimensional part {i}:')
    print(Array[i])

