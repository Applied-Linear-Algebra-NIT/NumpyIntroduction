import numpy as np

arr1 = np.array(
    [[1, 2],
     [3, 4]]
)

arr2 = np.array(
    [[6, 7],
     [8, 9]]
)

# arithmetic
print('< arithmetic >')
print('addition: \n', arr1 + arr2)
print('subtraction: \n', arr1 - arr2)
print('multiplication: \n', arr1 * arr2)
print('division: \n', arr1 / arr2)
print('\n')

# broadcasting
print('broadcasting')

arr1 = np.array(
    [[1],
     [2]]
)

arr2 = np.array([1, 2, 3])

print(arr1 + arr2)
print('***')
print(arr1 * arr2)

print('\n-----\n')

# reshaping & flattening
print('reshaping & flattening')

arr3 = np.arange(12)
arr3.resize((3, 2, 2))
print(
    'original 3-d array: \n', arr3,
    '\n\n',
    'reshaped 2-d array: \n',
    arr3.reshape((2, -1)),
    '\n\n',
    'flatten array: \n', arr3.flatten()
)
