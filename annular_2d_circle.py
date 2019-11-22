#All parameters are in Ang
#This is for 2d circular annular ap diffraction formula
import matplotlib.pyplot as plt
import numpy as np
import scipy.special as spl
q1=q2=np.linspace(-2*10**7,2*10**7,512)
q1,q2=np.meshgrid(q1,q2)
q=np.sqrt(q1**2+q2**2)
a=1*10**7
k=2*3.14/6000
f=1*10**10
e=0.6
m=a*k*q/f
n=k*a*q*e/f
z=1/(1-e**2)*((2*spl.j1(m)/m)-e*(2*spl.j1(n)/m))
plt.imshow(z**2)
#plt.plot(q1,z**2)
plt.show()
