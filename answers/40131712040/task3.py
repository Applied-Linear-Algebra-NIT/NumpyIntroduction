import numpy as np


array1 = np.array([[10, 20], [30, 40]])
array2 = np.array([[50, 60], [70, 80]])

sum_array = np.add(array1, array2)
print("sum of two array:")
print(sum_array)
print("\n")

subtraction_array = np.subtract(array1, array2)
print("subtraction of two array:")
print(subtraction_array)
print("\n")

multiplication_array = np.multiply(array1, array2)
print("multiplication of two array:")
print(multiplication_array)
print("\n")

division_array = np.divide(array1, array2)
print("Division of two array:")
print(division_array)

print("--------------------------------------------------")

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

V = np.array([10, 20, 30])

Sum = arr + V
print(Sum)

print("--------------------------------------------------")

array_3D = np.array([[[11, 22], [33, 44]], [[55, 66], [77, 88]]])

array_2D = array_3D.reshape(-1, array_3D.shape[-1])

array_1D = array_2D.flatten()

print("array_3D:")
print(array_3D)
print("\narray_2D:")
print(array_2D)
print("\narray_1D:")
print(array_1D)


