import numpy as np

print("Zeros Array:\n", np.zeros((2, 3)))
print("\nOnes Array:\n", np.ones((2, 2)))
print("\nArange Array (0 to 10 step 2):\n", np.arange(0, 10, 2))
print("\nLinspace Array (5 values between 0 and 1):\n", np.linspace(0, 1, 5))

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("\nMatrix A:\n", A)
print("Matrix B:\n", B)
print("\nMatrix Addition (A + B):\n", A + B)
print("\nMatrix Subtraction (A - B):\n", A - B)
print("\nElement-wise Multiplication (A * B):\n", A * B)
print("\nMatrix Multiplication (dot product):\n", np.dot(A, B))
print("\nTranspose of Matrix A:\n", A.T)