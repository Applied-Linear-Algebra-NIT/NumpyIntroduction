import numpy as np


oneD_array = np.array([1, 2, 3, 4, 5])
twoD_zero_array = np.zeros((3, 4))
threeD_one_array = np.ones((2, 3, 4))

# 1. Arithmetic Operations
print("Operations between \"two-dimensional\" & \"three-dimensional\" arrays:")
# Addition
print(f"Addition:\n{twoD_zero_array + threeD_one_array}\n")
# Subtraction
print(f"Subtraction:\n{twoD_zero_array - threeD_one_array}\n")
# Multiplication
print(f"Multiplication:\n{twoD_zero_array * threeD_one_array}\n")
# Division
print(f"Division:\n{twoD_zero_array / threeD_one_array}\n")


# 2. Broadcasting
vector = np.array([10, 20, 30])
result = twoD_zero_array + vector[:, np.newaxis]
print(f"Adding a vector to each column of the \"two-dimensional\" matrix:\n{result}\n")


# 3. Reshaping and Flattening
twoD_arr = threeD_one_array.reshape(-1, threeD_one_array.shape[-1])
print(f"The \"three-dimensional\" array in two-dimensional shape:\n{twoD_arr}\n")
oneD_arr = twoD_arr.flatten()
print(f"The \"three-dimensional\" array in one-dimensional shape:\n{oneD_arr}\n")
