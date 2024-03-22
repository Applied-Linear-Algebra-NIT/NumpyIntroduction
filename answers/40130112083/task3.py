import numpy as np

a = np.array([5,8,2])
b = np.array([3,1,9])
c = np.array([[[1,2,3], [5,6,7], [9,10,11]] , [[13,14,15], [17,18,19], [21,22,23]]])
d = np.reshape(c, (6, 3))

print(f'''addition : {np.add(a,b)}
subtraction : {np.subtract(a,b)}
multiplication : {np.multiply(a, b)}
division : {np.divide(a,b)}
broadcasting : 
{d + a}
reshape :
{d}
flatten : {c.flatten()}''')
