import numpy as np

temp = np.array([2, 4, 6, 8, 10])
print("third element : ",temp[2])

temp2 = np.array([[1, 2, 3, 7],
                [4, 5, 6, 8],
                [9, 10, 11, 12]])
print("temp[2][3] : ",temp2[2, 3])

print("-"*40,"\n")

temp3 = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])
print("Sub matrix : \n", temp3[:2, :2])

print("-"*40,"\n")

temp4 = np.array([[[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]],
                     
                     [[10, 11, 12],
                      [13, 14, 15],
                      [16, 17, 18]],
                     
                     [[19, 20, 21],
                      [22, 23, 24],
                      [25, 26, 27]]])

for i in range(temp4.shape[0]):
    print("Deminsion ", i+1, ":")
    print(temp4[i])