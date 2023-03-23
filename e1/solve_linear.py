import numpy as np

#Electrical system

R1 = 3.0
R2 = 2.0
R3 = 8.0

U1 = 10.0
U2 = 0.6

A = np.array([[1.0, -1.0, -1.0],
              [R1, R2, 0.0],
              [0.0, R2, -R3]])

b = np.array([[0.0], 
              [U1], 
              [U2]])

x = np.array([[0.0], 
              [0.0], 
              [0.0]])

n = 3

print("Before elimination: ")
print(A)
print(b)
print("--------------------")

#Gaussian Elimination
for j in range(n - 1):
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