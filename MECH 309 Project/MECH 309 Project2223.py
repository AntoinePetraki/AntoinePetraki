import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.cos(x)*np.cosh(x) + 1 

def f_prime(x):
    return -np.sin(x)*np.cosh(x) + np.cos(x)*np.sinh(x)



def newtonMethod(r0,eps):
    ''' Approximates the roots of a function using newtons method'''
    rK = []
    r1 = r0 + 2*eps
    while abs(r1 - r0) >= eps:
        r0 = r1 
        r1 = r0 - f(r0)/f_prime(r0)
        rK.append(r1)

    return r1

#print(newtonMethod(1.5, 0.0001)) #1.875
#print(newtonMethod(4.5,0.0001)) #4.694
[r1,r2] = 1.875, 4.694

#### Plotting
x = np.linspace(0,1,1000)

phi1 = np.sin(r1*x) + np.sinh(r1*x) + ((np.cos(r1) + np.cosh(r1))/(np.sin(r1) + np.sinh(r1)))*(np.cos(r1*x) - np.cosh(r1*x))

phi2 = np.sin(r2*x) + np.sinh(r2*x) + ((np.cos(r2) + np.cosh(r2))/(np.sin(r2) + np.sinh(r2)))*(np.cos(r2*x) - np.cosh(r2*x))

plt.plot(x,phi1,'r',x,phi2,'k')
plt.xlabel('x')
plt.ylabel(r'$\phi_i$')
plt.legend([r'$\phi_1$ ($r_1 = 1.875$)',r'$\phi_2$ ($r_2 = 4.694$)'])
plt.show()
