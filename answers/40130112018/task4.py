# Your Implemetation
import numpy as np

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print(m1)
print(m2)

print(np.dot(m1, m2))

print(np.linalg.det(m1))
print(np.linalg.inv(m1))

eigval, eigvec = np.linalg.eig(m1)
print(eigval)
print(eigvec)
