import numpy as np


# Explore more complex linear algebra operations, such as singular value decomposition (SVD)
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

u, s, vt = np.linalg.svd(A)

print(f"Matrix U:\n{u}\n")
print(f"Matrix Sigma:\n{np.diag(s)}\n")
print(f"Matrix VT:\n{vt}\n")


# Use NumPy to generate random samples and explore probability distributions
samples = np.random.normal(0, 1, 30)
print(f"The Probability Distributions are:\n{samples}")
