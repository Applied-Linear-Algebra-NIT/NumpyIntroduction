import numpy as np

# Part 1
matrix1 = np.arange(12).reshape(3,4)
matrix2 = np.arange(12).reshape(4,3)

print(f'\nDot multiplication of matrix:\n{matrix1}\n\nand matrix\n{matrix2}\n\nis equel to:\n{np.dot(matrix1, matrix2)}')

# Part 2
matrix = np.arange(4).reshape(2,2)
print(f'Determinant of matrix:\n{matrix}\n\nis: {np.linalg.det(matrix)}\n\nand the inverse of it is:\n{np.linalg.inv(matrix)}')

# Part 3
eigenvector , eigenvalue = np.linalg.eig(matrix)
print(f'\nwith EigenValues of :\n{eigenvalue}\n\nand EigenVectors of: {eigenvector}')
