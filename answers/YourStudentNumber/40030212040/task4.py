import numpy as np

# /-----------------Matrix Multiplication-----------------\

# creating two matrices:
matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[10, 11], [12, 13], [14, 15]])

# Performing the dot product :
dotProduct = np.dot(matrix1, matrix2)
print("dot product: ")
print(dotProduct)

# /-----------------Determinant and Inverse-----------------\

# creating a 2x2 matrix
twoByTwo = ([[1, 2], [3, 4]])

# Computing the determinant of the matrix
# linalg = sub-module for Linear Algebra O.O
determinant = np.linalg.det(twoByTwo)

# Computing the inverse of the matrix
inverse = np.linalg.inv(twoByTwo)
print("/-----------------\\")
print("2X2 Matrix:")
print(twoByTwo)
print("\nDeterminant: ", determinant)
print("\nInverse: ")
print(inverse)

# /-----------------Eigenvalues and Eigenvectors-----------------\

# Computing the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(twoByTwo)

print("/-----------------\\")
print("Matrix:")
print(twoByTwo)
print("\nEigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)
