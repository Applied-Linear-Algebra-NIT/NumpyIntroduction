import numpy as np

a = np.array([[1, 2],
            [3, 4]])
b = np.array([[5, 6],
            [7, 8]])
print("Multiplication :\n", np.multiply(a,b))

print("-"*40,"\n")

x = np.array([[1, 2], [3, 4]])
print("x : \n",x)

d = np.linalg.det(x)
print("determinant of x :\n", d)

i = np.linalg.inv(x)
print("inverse of x : \n", i)

print("-"*40,"\n")

x = np.array([[4, 3], [2, 1]])
print("x :\n", x)
eigenvalus, eigenvectors = np.linalg.eig(x)
print("EigenValues of x :\n", eigenvalus)
print("EigenVectors of x: \n", eigenvectors)