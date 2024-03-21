import numpy as np

# Matrix Multiplication
matrix1 = np.array([[1, 2],
                    [3, 4]])

matrix2 = np.array([[5, 6],
                    [7, 8]])

dot_product = np.dot(matrix1, matrix2)
print("Matrix Multiplication (Dot Product):")
print(dot_product)

# Determinant and Inverse
matrix_2x2 = np.array([[1, 2],
                       [3, 4]])

determinant = np.linalg.det(matrix_2x2)
inverse = np.linalg.inv(matrix_2x2)

print("\nDeterminant of the matrix:")
print(determinant)

print("\nInverse of the matrix:")
print(inverse)

# Eigenvalues and Eigenvectors
matrix_square = np.array([[2, -1],
                          [-1, 2]])

eigenvalues, eigenvectors = np.linalg.eig(matrix_square)

print("\nEigenvalues of the matrix:")
print(eigenvalues)

print("\nEigenvectors of the matrix:")
print(eigenvectors)