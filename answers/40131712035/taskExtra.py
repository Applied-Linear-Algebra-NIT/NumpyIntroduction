import numpy as np
import matplotlib.pyplot as plt

# SVD:
matrix = np.array([[1, 2], [3, 4], [5, 6]])
U, S, Vt = np.linalg.svd(matrix, full_matrices=False)

print("U (left singular vectors):")
print(U)
print("\nS (singular values):")
print(S)
print("\nVt (right singular vectors, transposed):")
print(Vt)

# Probability Distributions:
# 1.Normal Distribution:
mu, sigma = 0, 0.1
samples_normal = np.random.normal(mu, sigma, 1000)
plt.hist(samples_normal, bins=30, density=True)
plt.title('Normal Distribution')
plt.show()
# 2.Binomial Distribution:
n, p = 10, 0.5
samples_binomial = np.random.binomial(n, p, 1000)
plt.hist(samples_binomial, bins=max(samples_binomial), density=True)
plt.title('Binomial Distribution')
plt.show()
# 3.Poisson Distribution:
lam = 5
samples_poisson = np.random.poisson(lam, 1000)
plt.hist(samples_poisson, bins=max(samples_poisson), density=True)
plt.title('Poisson Distribution')
plt.show()
