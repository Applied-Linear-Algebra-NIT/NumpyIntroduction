import numpy as np

arr1 = np.array([1, 2, 3, 4])

print('Descriptive Statistics')

print('mean: ', arr1.mean())
print('median: ', np.median(arr1))
print('variance: ', np.var(arr1))
print('standard deviation: ', np.std(arr1))


print('\n-----\n')
arr2 = np.array([2, 3, 5, 6])

print('Correlation of arr1 and arr2: ')
print(np.correlate(arr1, arr2))
