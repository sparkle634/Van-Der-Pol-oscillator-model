from scipy.special import gamma
import math
import numpy as np
import matplotlib.pyplot as plt

def adam(f,t,y,h,k,mu):
  def a_jk(k,j,mu):
    if j==0:
      return (((k-1)**(1+mu))-(k-mu-1)*(k**mu))/gamma(2+mu)
    elif 1 <=j<=k-1:
      return (((k-j+1)**(1+mu)) + ((k-j-1)**(1+mu)) -2*((k-j)**(1+mu)))/gamma(2+mu)
    elif j==k:
      return 1/gamma(2+mu)
    else:
      return 0

  def b_jk(k,j,mu):
    return ((k-j)**mu - (k-1-j)**mu)/gamma(1+mu)

  sum1,sum2 = 0, 0
  for j in range(k):
    sum1 += b_jk(k,j,mu)*f(t[j],y[j],mu)
    sum2 += a_jk(k,j,mu)*f(t[j],y[j],mu)
    
  initial = np.sum(t[k]**j/math.factorial(j)*y0 for j in range(math.ceil(mu)))
  
  #Predictor
  yk_0 = initial  + (h**mu)*sum1
  #Corrector
  yk_1 =initial + (h**mu)*sum2 + (h**mu)*a_jk(k,k,mu)*f(t[k],yk_0,mu)

  return yk_1

def f(t,y,B,K,w,mu):
  return np.array([y[1], (K*y[0]**2- B)*y[1] - (w**mu)*y[0] + xi])

B = -5
K = 25
w = 120
xi = 0
N = 100
h = 10/N
t = np.linspace(0,10,N+1)
y0 = np.array([0.1,0])
func = lambda t,y,mu: f(t,y,B,K,w,mu)

yout = np.zeros((N+1,2))
yout[0] = y0
for k in range(1,N+1):
  yout[k] = adam(func,t = t,y = yout[:k],h = h,k = k,mu = 1)

plt.plot(yout[:,0],marker='o')  
