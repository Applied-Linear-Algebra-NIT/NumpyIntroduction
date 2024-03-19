import numpy as np
#Matrix Multiplication
#creaating matrix
first=np.array([[3, 4], [5, 6]])
second=np.array([[1, 2], [4, 8]])
#dot product
multiplication= np.dot(first,second)
print(multiplication)

#Determinant and Inverse
#creating matrix
matrix= np.array([[1, 2], [3, 4]])
#the determinant of the matrix
determinant = np.linalg.det(matrix)
# the inverse of the matrix
inverse = np.linalg.inv(matrix)
print("\nDeterminant of the matrix:",determinant)
print("\nInverse of the matrix:",inverse)

