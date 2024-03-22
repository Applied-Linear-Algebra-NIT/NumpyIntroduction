import numpy as np

a = [1,2,3,4,5,6,7]
b = np.array(a)
print(f'''dimension : {b.ndim}
shape : {b.shape}
size : {b.size}
data type : {b.dtype}
sum : {b.sum()}''')


c = np.array([[0,0,0,0], [0,0,0,0], [0,0,0,0]])
print(f'''dimension : {c.ndim}
shape : {c.shape}
size : {c.size}
data type : {c.dtype}
sum : {c.sum()}''')


d = np.array([[[1,1,1,1], [1,1,1,1], [1,1,1,1]] , [[1,1,1,1], [1,1,1,1], [1,1,1,1]]])
print(f'''dimension : {d.ndim}
shape : {d.shape}
size : {d.size}
data type : {d.dtype}
sum : {d.sum()}''')
