import numpy as np

# my 1-d array
arr1 = np.array([1, 2, 3, 4])

arr2 = np.array(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
)

# my 2-d array

# assignment 1 ( Indexing )
print('Indexing')
print(arr1[2], end='\n***\n')  # 3rd element of 1-d array
print(arr2[1, 2], end='\n\n-----\n\n')  # 3rd element of 2nd row in 2-d array

# assignment 2 ( Slicing )
print('Slicing')
print(arr2[:2, :2], end='\n\n-----\n\n')

# assignment 3 ( Iterating )
print('Iterating')
arr3 = np.arange(0, 12)
arr3.resize((3, 2, 2))

for i in arr3:
    print(i, end='\n *** \n')
