import numpy as np

A = np.array([[210.5665, 215.9568, 375.3999],
              [309.2944, 317.1409, 550.7982],
              [227.6848, 232.4327, 403.2554]])

b = np.array([[-0.4816],
              [-0.7068],
              [-0.5182]])

# a) Solve the original system Ax = b
xref = np.linalg.solve(A, b)
print("Solution to Ax = b: ")
print(xref)
print("---------------------")

# b) Perturbations

# disp('Problem 3b')
# kmax=0;
# for n=1:1000
#  db=0.02*rand(3,1)-0.01;
#  dx=A\(b+db)-xref;
#  k=norm(dx)*norm(b)/norm(xref)/norm(db);
#  if k>kmax
#   kmax=k;
#  end
# end
# kmax

kmax = 0.0
for i in range (1, 1000):
    db = np.random.random(1) * 0.01
    dx = np.linalg.solve(A, b + db - xref)
    k = (np.linalg.norm(dx) * np.linalg.norm(b)) / (np.linalg.norm(xref) * np.linalg.norm(db))
    if k > kmax:
        kmax = k

print("Max k = ", kmax) # Very sensitive to perturbations??

# c) Compute the condition number k(A) = cond(A) * cond(A^{-1})

k_A = np.linalg.cond(A) * np.linalg.cond(np.linalg.inv(A))

print("K(A) = ", k_A) #Also very large. >10^{8} => ill-conditioned
