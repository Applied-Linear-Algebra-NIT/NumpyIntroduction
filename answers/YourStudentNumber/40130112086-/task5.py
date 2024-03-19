import numpy as np
#Descriptive Statistics

#creating array
array = np.array([8, 10, 15, 1, 5, 9, 34])

#Calculating mean, median, variance, and standard deviation
mean= np.mean(array)
median= np.median(array)
variance= np.var(array)
std= np.std(array)
print("Mean:", mean)
print("Median:", median)
print("Variance:", variance)
print("Standard Deviation:",std)


#Correlation

#creating arrays
first_array = np.array([3, 2, 1, 4, 5])
second_array = np.array([5, 4, 1, 2, 3])

#Calculating the correlation coefficient
correlation_coefficient = np.corrcoef(first_array,second_array)
print("\nCorrelation Coefficient:\n",correlation_coefficient)

