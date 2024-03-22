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

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

print(np.add(a, b))
print(np.subtract(b, a))
print(np.multiply(a, b))
print(np.divide(b, a))

vector = np.array([10, 20, 30, 40])

print(two_d_array + vector)

r3d = three_d_array.reshape(-1, three_d_array.shape[-1])
print(r3d)

flat = r3d.flatten()
print(flat)