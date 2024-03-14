import numpy as np

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

result = np.dot(matrix1, matrix2)

print("matrix1:")
print(matrix1)
print("\nmatrix2:")
print(matrix2)
print("\ndot mul:")
print(result)

# --------------------------------------

matrix = np.array([[1, 2],
                   [3, 4]])

determinant = np.linalg.det(matrix)
inverse = np.linalg.inv(matrix)

print("matrix:")
print(matrix)
print("determinant: ", determinant)
print("inverse:")
print(inverse)

# ---------------------------------------

Array = np.array([[4, 2],
                [2, 4]])
eigenvalues, eigenvectors = np.linalg.eig(Array)
print("value:")
for value in eigenvalues:
    print(value)

print("\nvector:")
for vector in eigenvectors:
    print(vector)
