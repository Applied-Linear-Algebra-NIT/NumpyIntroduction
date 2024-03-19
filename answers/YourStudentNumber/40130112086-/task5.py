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
