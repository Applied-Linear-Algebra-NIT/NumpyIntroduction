import numpy as np

# Part 1
array3D = np.arange(64).reshape(4,4,4)
array1 = np.arange(5)
array2 = np.arange(5, 10)
addition = np.add(array1, array2)
print(f'First array: \n{array1} \nsecond array: \n{array2}\nsum of the two array:\n{addition}')

subtraction = np.subtract(array1, array2)
print(f'subtraction of the two array:\n{subtraction}')

multiplication = np.multiply(array1, array2)
print(f'multiplication of the two array:\n{multiplication}')

division = np.divide(array1, array2)
print(f'division of the two array:\n{division}')

# Part 2
vector = np.arange(5) # Horizontal Vector
vector = vector.reshape(5, 1) # Vertical Vector
array2D = np.arange(25).reshape(5,5)
result = array2D + vector
print(f'\n\n2D array:\n{array2D}\n')
print(f'vertical vector:\n{vector}\n')
print(f'result:\n{result}\n')

# Part 3
reshaped_2d_array = array3D.reshape(-1, 4)
print(f'3D array is:\n{array3D}\nreshaped to 2D array:\n{reshaped_2d_array}\n')
reshaped_1d_array = reshaped_2d_array.reshape(-1, 1).transpose(1, 0).reshape(-1)
print(f'now flattened to 1D arrray:\n{reshaped_1d_array}')
