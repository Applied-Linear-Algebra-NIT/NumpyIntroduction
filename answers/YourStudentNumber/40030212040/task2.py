import numpy as np

# /-----------------Indexing-----------------\
# One-dimensional array:
pList = [1,2,3,4,5,6]
npList = np.array(pList)

# accessing the third element:
thirdElement = npList[2]

# -----------------------------------------------

# Two-dimensional matrix:
threeByFourMatrix = np.zeros((3, 4))

# accessing the [2, 3] element:
element2And3 = threeByFourMatrix[2, 3]

# /-----------------Slicing-----------------\

# General syntax for slicing in NumPy: {array[start:stop:step]}
# Extracting specific rows or columns from a 2D array: 
#           array[start_row:end_row, start_col:end_col] 
subMatrix = threeByFourMatrix[:2, :2]

# -----------------------------------------------
tDM =  np.ones((2,3,4))