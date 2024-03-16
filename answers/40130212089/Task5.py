import numpy as np

array1 = np.random.randint(high=100, low=10, size=10) # rnadom array of size 10
print(f'Array:\n{array1}\n\nMean: \n{np.mean(array1)}\n\nMedian:\n{np.median(array1)}\n\nVariance:\n{np.var(array1)}\n\nStandard Deviation:\n{np.std(array1)}')

# Part 2
array2 = np.random.randint(high=100, low=10, size=10) # rnadom array of size 10
print(f'Correlation Coefficient of array\n{array1}\nand \n{array2}\n is equal to: \n{np.corrcoef(array1, array2)}')