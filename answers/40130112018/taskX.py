# Your Implemetation
import numpy as np
import matplotlib.pyplot as plt

############# TASK 1 #############
one_d_array = np.array([1, 2, 3, 4, 5])

print(one_d_array)

# 3 by 4 array
two_d_array = np.array([[1, 2, 3, 10], [4, 5, 6, 11], [7, 8, 9, 12]])

print(two_d_array)


# 2 by 3 by 4 array

three_d_array = np.array(
    [
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
        [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]],
    ]
)

print(three_d_array)


############# TASK 2 #############

print(one_d_array[2])
print(two_d_array[2, 3])

sub_array = two_d_array[:2, :2]
print(sub_array)


for i in three_d_array:
    print(i)


############# TASK 3 #############

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

print(np.add(a, b))
print(np.subtract(b, a))
print(np.multiply(a, b))
print(np.divide(b, a))

vector = np.array([10, 20, 30, 40])

print(two_d_array + vector)

r3d = three_d_array.reshape(-1, three_d_array.shape[-1])
print(r3d)

flat = r3d.flatten()
print(flat)


############# TASK 4 #############

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print(m1)
print(m2)

print(np.dot(m1, m2))

print(np.linalg.det(m1))
print(np.linalg.inv(m1))

eigval, eigvec = np.linalg.eig(m1)
print(eigval)
print(eigvec)


############# TASK 5 #############

a = np.array([1, 2, 3, 4, 5])

print(np.mean(a))
print(np.median(a))
print(np.var(a))
print(np.std(a))

b = np.array([6, 7, 8, 9, 10])

corr_coef = np.corrcoef(a, b)

print(corr_coef)


############# TASK 6 #############

x = np.array(range(100))
y = x ** 2

fitted = np.polyfit(x, y, 2)

print(fitted)

plt.plot(x, y)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Y = X^2")

plt.show()