import numpy as np

l = [1, 2, 3]
a = np.array(l)
print(a)
print("deminsion of a : ", a.shape)
print("Size of a : ", a.size)
print("Data type of elements of a : ", a.dtype)
print("Sum of elements of a : ", np.sum(a), "\n")

z = np.zeros((3, 4))
print(z)
print("deminsion of z : ", z.shape)
print("Size of z : ", z.size)
print("Data type of elements of z : ", z.dtype)
print("Sum of elements of z : ", np.sum(z), "\n")

o = np.ones((2, 3, 4))
print(o)
print("deminsion of o : ", o.shape)
print("Size of o : ", o.size)
print("Data type of elements of o : ", o.dtype)
print("Sum of elements of o : ", np.sum(o))