from scipy.interpolate import lagrange
from numpy import *
import matplotlib.pyplot as plt
def jop(x):
    return 2*x**3-15*x+5
x = array([-3, -2, 1, 3],dtype =float)
y = array([-4, 19, -8, 14], dtype = float)
U = array([-1.5, 0.5, 1.5, 2])

def L(x, y, k):
    summa=0
    for g in range (len(y)):
        p1=1
        p2=1
        for i in range (len(y)):
            if i==g:
                p1 *= 1
                p2 *= 1
            else:
                p1*=(k-x[i])
                p2*=(x[g]-x[i])
        summa += y[g]*p1/p2
    return summa
xnew = linspace (min(x), max(x))
ynew = [L(x,y,i) for i in xnew]
plt.plot(x, y, 'o', xnew, ynew)
plt.title('LB_7 Ihor Uchiha')
plt.legend(loc='upper left')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

f = lagrange(x, y)
fig = plt.figure(figsize = (10,8))
plt.plot(xnew, f(xnew), 'b', x, y, 'ro')
plt.title('Lagrange Polynomial')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()