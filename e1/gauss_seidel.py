import numpy as np

A = np.array([[10.2, 0.0,  -1.1],
             [0.1,  12.0,  0.0] ,
             [0.1,  0.2,  -9.3 ]])

b = np.array([[1],
             [2],
             [3]])

x = np.array([[1],  # x[0] = u
              [1],  # x[1] = v
              [1]]) # x[2] = w

k = 10 # Iterations
n = A.shape[0]

print("'Exact' Solution: ")
print(np.linalg.solve(A,b))
print("--------------------")

D = np.diagonal(A)
D = np.array([[D[0], 0.0,  0.0],
             [0.0,   D[1], 0.0],
             [0.0,   0.0,  D[2]]])
R = np.subtract(A, D)
U = np.triu(R)
L = np.tril(R)

Dinv = np.linalg.inv(D)

# Gauss - Seidel method
for i in range(k):
    # Calculate 1 row each. 
    x = np.multiply(Dinv, b[0] - np.multiply(U[0], x[0]) - np.multiply(L[0], x[0]))
    x = np.multiply(Dinv, b[1] - np.multiply(U[1], x[1]) - np.multiply(L[1], x[1]))
    x = np.multiply(Dinv, b[2] - np.multiply(U[2], x[2]) - np.multiply(L[2], x[2]))

print("Gauss-Seidel solution: ")
print(np.linalg.solve(A,b))
print("--------------------")

"""
Task B: 
Give a sufficient condition for the Gauss{Seidel method to converge
for a general system Ax = b. Check if your condition is fulfilled in the
current example. Here, the Matlab function norm is handy.
"""

"""
Convergence of the gauss-seidel method follows from the spectral radius of the matrix
    (L + D)^{-1}U
If the spectral radius, which is the maximum of the eigenvalues of the matrix, is strictly less than one,
then the gauss-seidel solution converges to the solution for Ax = b
"""

eig = np.linalg.eigvals(np.multiply(np.linalg.inv(L + D), U))
spectral_radius = np.abs(np.max(eig))
print("The spectral radius of the matrix is: ", spectral_radius)