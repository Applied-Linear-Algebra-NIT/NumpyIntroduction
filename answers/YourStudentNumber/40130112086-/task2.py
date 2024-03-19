import numpy as np
#indexing

#Accessing the third element
array=[1,2,3]
third_element=array[2]
#Accessing the element at position [2, 3]
matrix = np.array([[2,4,6], [8,10,12]])
elemet=matrix[1,2]

#Slicing

#Extracting a 2x2 sub-matrix
sub=matrix[:2,:2]

#Iterating

three_dimensional_array = np.arange(24).reshape(2, 3, 4)
for i in range(three_dimensional_array.shape[0]):
    print("Section",i+1,":")
    print(three_dimensional_array[i])
