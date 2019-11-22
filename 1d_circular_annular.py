#All parameters are in Ang
#This is for circular annular ap in 1d
import matplotlib.pyplot as plt
import numpy as np
import scipy.special as spl
q1=np.linspace(-2*10**7,2*10**7,512)
a=1*10**7
k=2*3.14/6000
f=10**10
e=0.6
m=q1*k*a/f
n=k*a*e*q1/f
z=1/(1-e**2)*((2*spl.j1(m)/m)-(e)*(2*spl.j1(n)/m))
plt.xlabel('q1*a*k/f')
plt.ylabel('intensity')
plt.plot(q1*a*k/f,z**2)
plt.show()
