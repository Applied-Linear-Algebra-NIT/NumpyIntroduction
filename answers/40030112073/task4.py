import numpy as np

# Matrix Multiplication (Dot Product)
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
dot_product = np.dot(matrix_a, matrix_b)

# Determinant and Inverse of a (2x2) Matrix
matrix_c = np.array([[2, 1], [1, 2]])
determinant = np.linalg.det(matrix_c)
inverse = np.linalg.inv(matrix_c)

# Eigenvalues and Eigenvectors of a Square Matrix
eigenvalues, eigenvectors = np.linalg.eig(matrix_c)

# Results
print("Dot Product:\n", dot_product)
print("\nDeterminant of the matrix:", determinant)
print("Inverse of the matrix:\n", inverse)
print("\nEigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
