import numpy as np

array1D = np.array([0, 1, 2, 3, 4])
array2D = np.zeros((3, 4))
# Part 1
print('Task 2')
print(f'The third element of the one dimensional array: {array1D[2]}')
print(f'The element at position [2, 3] in tow dimensional array: {array2D[2, 3]}')

# Part 2
array2D = np.arange(16).reshape(4,4) 
sub_matrix = array2D[np.ix_([0,1],[0,1])]
print(f'2x2 matrix from upper left corner of the tow dimensional matrix:\n {sub_matrix}')

# Part 3
array3D = np.arange(64).reshape(4,4,4) 
print(f'\niterating over the 3D matrix: ')

for x in array3D:
    for y in x:
        for z in y:
            print(z, end = " ")
        print()
    print()
    