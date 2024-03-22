import numpy as np


# def to print array data    
def arr_data(arr):
    print(f"array:{arr}\nsum:{arr.sum()}\ndimension:{arr.ndim}\nshape:{arr.shape}\nsize:{arr.size}\ntype:{type(arr.dtype)}\n------------------")


arr_1 = np.array([4, 0, 0, 3, 0, 1, 1, 2, 0])

arr_data(arr_1)

arr_2 = np.zeros(shape=(3, 4))

arr_data(arr_2)

arr_3 = np.ones((2, 3, 4))

arr_data(arr_3)
