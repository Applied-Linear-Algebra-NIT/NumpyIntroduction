import numpy as np

# 1.Matrix Multiplication:
matrix1 = np.array([[28, 9], [13, 83]])
matrix2 = np.array([[1, 2], [3, 4]])
print("Multiplication Result:", np.dot(matrix1, matrix2))

# 2.Determinant And Inverse:
print("Determinant:", np.linalg.det(matrix1))
print("Inverse:", np.linalg.inv(matrix1))

# 3.Eigenvalues and Eigenvectors:
eigenvalues, eigenvectors = np.linalg.eig(matrix1)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
