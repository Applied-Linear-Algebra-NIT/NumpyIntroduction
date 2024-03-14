import numpy as np

array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

sum_array = np.add(array1, array2)
print("Sum:")
print(sum_array, "\n")

sub_array = np.subtract(array1, array2)
print("Sub:")
print(sub_array, "\n")

mul_array = np.multiply(array1, array2)
print("Mul:")
print(mul_array, "\n")

div_array = np.divide(array1, array2)
print("Div:")
print(div_array)

# ---------------------------------------------

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

vector = np.array([1, 2, 3])

result = matrix + vector

print(result)

# ---------------------------------------------

array_3d = np.random.randint(1, 10, (3, 3, 3))
print("3D:")
print(array_3d)

array_2d = array_3d.reshape(-1, array_3d.shape[-1])
print("\n2D:")
print(array_2d)

array_1d = array_2d.flatten()
print("\n1D:")
print(array_1d)
