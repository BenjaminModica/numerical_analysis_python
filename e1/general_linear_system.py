import numpy as np

A = np.random.random((10,10))
b = np.random.random((10,1))
x = np.zeros((10,1))
print(A)
print(b)

AA = A.copy()
bb = b.copy()

n = A.shape[0]

print("Before elimination: ")
print(A)
print(b)
print("--------------------")

#Gaussian Elimination
for j in range(n - 1): #for (int i = 0, i < length, i++)
    if A[j, j] == 0: 
        print("Error: pivot is zero")
    for i in range(j + 1, n):
        mult = A[i, j] / A[j, j]
        for k in range(j, n):
            A[i, k] = A[i, k] - mult * A[j, k]
        b[i] = b[i] - mult * b[j]

print("After elimination: ")
print(A)
print(b)
print("--------------------")

#Back Substitution
for i in range(n - 1, -1, -1):
    for j in range(i, n):
        b[i] = b[i] - A[i, j]*x[j]
    x[i] = b[i] / A[i, i]

print("Solution: ")
print(x)
print("--------------------")

print("Solution with linalg: ")
print(np.linalg.solve(AA,bb))
print("--------------------")
