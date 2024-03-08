import numpy as np
# /-----------------Arithmetic Operations-----------------\


# -----------------------------------------------

# /-----------------Reshaping and Flattening-----------------\

# Three-dimensional matrix:
tDM =  np.ones((2,3,4))

# The general syntax of the reshape() function is:
#           numpy_array.reshape(new_shape)
# new_shape is the desired new shape specified as a tuple of integers.

# One of the dimensions in the new shape can be -1, which means it will be 
# automatically calculated based on the size of the array and the other dimensions.
twoD = tDM.reshape(-1, 4)

# Flatten the two-dimensional array into a one-dimensional array
oneD = twoD.flatten()

print("The original array: \n\n", tDM)
print("The reshaped array: \n\n", twoD)
print("The flatten array: \n\n", oneD)

# Note that the number of the elements should be the same 