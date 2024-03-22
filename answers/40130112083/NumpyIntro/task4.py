import numpy as np

a = np.array([[1,1], [2,3]])
b = np.array([[2,0],[1,2]])
print(f'''Matrix Multiplication :
{np.dot(a, b)}
Determinant and Inverse :
{np.linalg.det(a)}
{np.invert(a)}
Eigenvalues and Eigenvectors : {np.linalg.eigvals(a)} 
{np.linalg.eig(a)}''')