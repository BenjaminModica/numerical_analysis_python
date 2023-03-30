import numpy as np

def newtons_divided_differences(x, y, n, c):

    c[0] = y[0]

    for j in range(n - 1):
        for i in range(n - 1 - j):
            y[i] = ( y[i + 1] - y[i] ) / ( x[i + 1 + j] - x[i] )

            if i == 0: c[i + 1 + j] = y[i] 

            #print(y[i])
    
    return c

def horner_evaluation(x_eval, c, d, x):
    yy = c[d]
    for i in range(d):
        yy = yy*(x_eval - x[d - 1 - i]) + c[d - i - 1]
    return yy

# Oatmeal recipe problem
x = np.array([1.0, 2.0, 4.0]) #Number of servings
y = np.array([2.5, 4.5, 9.0]) #Volume of water
c = np.array([0.0, 0.0, 0.0]) #Fill with coefficients

polyfit = np.polyfit(x, y, 2)
polyval = np.polyval(polyfit, 100)

print("Sanity check?: ", polyval)

xx = np.copy(x)
#yy = np.copy(y)

n = len(x)

c = newtons_divided_differences(x, y, n, c)

d = 2 #Degree of polynomial
x_eval = 100

#print(c)

value = horner_evaluation(100, c, d, x)

print("Answer to a) : ", value)

