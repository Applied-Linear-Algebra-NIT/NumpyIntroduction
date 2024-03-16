import numpy as np

# /-----------------Indexing-----------------\
# One-dimensional array:
pList = [1,2,3,4,5,6]
npList = np.array(pList)

# accessing the third element:
thirdElement = npList[2]

print("Third element of the One-dimensional array: ")
print(thirdElement)
# -----------------------------------------------

# Two-dimensional matrix:
threeByFourMatrix = np.zeros((3, 4))

# accessing the [2, 3] element:
element2And3 = threeByFourMatrix[2, 3]

print("\n[2,3] element of the Two-dimensional array: ")
print(element2And3)
print("\n/-----------------\\")
# /-----------------Slicing-----------------\

# General syntax for slicing in NumPy: {array[start:stop:step]}
# Extracting specific rows or columns from a 2D array: 
#           array[start_row:end_row, start_col:end_col] 
subMatrix = threeByFourMatrix[:2, :2]

print("\nSliced sub-matrix: \n")
print(subMatrix)
print("\n/-----------------\\")
print()

# /-----------------Iterating-----------------\

# Three-dimensional matrix:
tDM =  np.ones((2,3,4))

print("Iteration: ")

# Iterating over the first dimension :
for i in range(tDM.shape[0]):
    # Printing each two-dimensional section
    print(f"{i+1}. ")
    print(tDM[i])
    print()
    