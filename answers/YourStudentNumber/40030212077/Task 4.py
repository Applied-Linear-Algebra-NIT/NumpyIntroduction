import numpy as np


matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])


# 1. Matrix Multiplication
dot_matrix = np.dot(matrix1, matrix2)
print(f"The dot product between two matrices:\n{dot_matrix}\n")

# 2. Determinant and Inverse
# Determinant
determinant = np.linalg.det(matrix1)
print(f"The determinant of the (2 times 2) matrix:\n{determinant}\n")

# Inverse
inverse_matrix = np.linalg.inv(matrix1)
print(f"The inverse of the (2 times 2) matrix:\n{inverse_matrix}\n")


# 3. Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix1)
print(f"The eigenvalues of the square matrix:\n{eigenvalues}\nThe eigenvectors of the square matrix:\n{eigenvectors}\n")


