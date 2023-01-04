import numpy as np
A = np.array([[1, 1], [2, 2]])
B = np.array([[3, 3], [4, 4]])
C = np.array([[5, 5], [6, 6]])
mul = np.multiply(A, B)
bsq = np.multiply(B, B)
div = np.divide(C, 4)

res = np.subtract(np.add(mul, np.multiply(4, bsq)), div)
print("Result Matrix:\n", res)


