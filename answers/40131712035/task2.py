import task1
import numpy as np

# 1.Indexing:
print(task1.oneDimensionalArray[2])
print(task1.twoDimensionalArray[2, 3])

# 2.Slicing:
print(task1.twoDimensionalArray[0:2, 0:2])

# 3.Iterating:
for x in task1.threeDimensionalArray:
    print(x, end="\n")
