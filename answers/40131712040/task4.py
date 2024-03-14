import numpy as np

matrix1 = np.array([[10, 20], [30, 40]])
matrix2 = np.array([[50, 60], [70, 80]])

result = np.dot(matrix1, matrix2)

print("* matrix1:")
print(matrix1)
print("* matrix2:")
print(matrix2)
print("* result:")
print(result)

print("--------------------------------------------------")

matrix = np.array([[10, 20],
                   [30, 40]])

determinant = np.linalg.det(matrix)
inverse = np.linalg.inv(matrix)

print("matrix:")
print(matrix)
print("determinant: ", determinant)
print("inverse of matrix:")
print(inverse)

print("--------------------------------------------------")

Array = np.array([[11, 22],
              [20, 10]])

eigenvalues, eigenvectors = np.linalg.eig(Array)
print("value:")
for value in eigenvalues:
    print(value)

print("\nvector:")
for vec in eigenvectors:
    print(vec)
