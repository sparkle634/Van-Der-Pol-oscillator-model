import numpy as np
import matplotlib.pyplot as plt

def RK4(f, x0, t, h):
  k1 = f(t , x0)
  k2 = f(t+h/2 , x0 + h*k1/2)
  k3 = f(t+h/2 , x0 + h*k2/2)
  k4 = f(t+h , x0 + h*k3)

  x1 = x0 + h*(k1+2*k2+2*k3+k4)/6
  return x1

def func3(t,x):
  return np.array([x[1] , (k*x[0]**2 - b)*x[1] - x[0]*w**2 ])
N = 1000
h = 50/N
t = np.linspace(0,50,N+1)
k = 25
b = -5
w = 120/(2*np.pi)
x = np.array([0.1,0])

xout = [x]

for i in range(1,N+1):
  xout.append(RK4(func3,x0 = xout[i-1], t = t, h = h))
xout = np.vstack(xout)
plt.plot(xout[:15,0],marker='o')
