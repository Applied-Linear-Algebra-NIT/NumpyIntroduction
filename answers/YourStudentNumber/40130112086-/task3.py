import numpy as np
#Arithmetic Operations
#creating arrays
First_array = np.array([[4, 2], [3, 9]])
Second_array = np.array([[2, 1], [8, 3]])
#operations
addition=First_array+Second_array
subtraction=First_array-Second_array
multiplication=First_array*Second_array
division=First_array/Second_array
print("addition",addition)
print("Subtraction",subtraction)
print("multiplication",multiplication)
print("division",division)

#Broadcasting:
#Demonstrating array broadcasting
#creating matrix and vector
matrix = np.array([[9, 10, 31], [0, 6, 55]])
vector = np.array([3,6])
broadcasting = matrix + vector[:, np.newaxis]
print("\n",broadcasting)

