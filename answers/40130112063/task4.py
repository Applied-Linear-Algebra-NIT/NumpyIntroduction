import numpy as np

matrix_1 = np.array([[1, 2], [3, 4], [5, 6]])
matrix_2 = np.array([[7, 8, 9], [10, 11, 12]])
matrix_3 = np.array([[3, 4], [1, 2]])

# Matrix Multiplication
dot_result = np.dot(matrix_1, matrix_2)

print('matrix 1:\n', matrix_1)
print('matrix 2:\n', matrix_2)

print("Dot product of matrix1 and matrix2:\n", dot_result)

# Determinant and Inverse
print('matrix 3:\n', matrix_3)
determinant = np.linalg.det(matrix_3)
print('Determinant of matrix 3:', determinant)
inverse = np.linalg.inv(matrix_3)
print("Inverse of matrix 3:\n", inverse)

# Eigenvalues and Eigenvectors
w, v = np.linalg.eig(matrix_3)
print("Eigenvalues of matrix 3:\n", w)
print("Eigenvector of matrix 3:\n", v)

