import numpy as np

x = np.array([[1, 2],
                [3, 4]])
y = np.array([[5, 6],
                [7, 8]])

print("x : \n",x, "\ny : \n", y)
print("Addition :\n",x+y)
print("Subtraction :\n",x-y)
print("Multiplication :\n", x*y)
print("Devision :\n",np.divide(x, y))

print("-"*40,"\n")

matrix = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

print("Original matrix: \n", matrix)
vector = np.array([1, 2, 3])
print("Vector :\n", vector)

for i in range(len(matrix[0])):
    matrix[:, i] += vector
print("new matrix :\n", matrix)

print("-"*40,"\n")


arr_3d = np.array([
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8]
                ],
                [
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]
                ]
])

print("Original 3D Array:")
print(arr_3d)
print("Shape of Original 3D Array:", arr_3d.shape)


arr_2d = arr_3d.reshape(-1, arr_3d.shape[-1])
print("\nReshaped 2D Array:")
print(arr_2d)
print("Shape of Reshaped 2D Array:", arr_2d.shape)


arr_1d_flatten = arr_2d.flatten()
print("\nFlattened 1D Array :")
print(arr_1d_flatten)