import numpy as np

arr1 = np.array(
    [[1, 2],
     [3, 4]], dtype='f'
)

arr2 = np.array(
    [[3, 2],
     [1, 5]]
)

print('matrix multiplication: \n')
print('dot operation: \n', np.dot(arr1, arr2))

print('\n-----\n')
print('determinant & inverse')
print('determinant of arr1: ', np.linalg.det(arr1))
print('inverse of arr2: \n', np.linalg.inv(arr2))

print('\n-----\n')
print('Eigenvalues and Eigenvectors')
Eigenvalues, Eigenvectors = np.linalg.eig(arr1)
print('Eigenvalues of arr1: \n', Eigenvalues)
print('***')
print('Eigenvectors of arr1: \n', Eigenvectors)
