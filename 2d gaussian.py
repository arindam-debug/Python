#This program is for 2d periodic gaussian and its fft
import scipy.fftpack as fftim
import matplotlib.pyplot as plt
import numpy as np
import scipy.special as spl
x=y=np.linspace(-20,20,1024)
from scipy.interpolate import interp1d
v=np.zeros(1048576).reshape(1024,1024)
x,y=np.meshgrid(x,y)
sigma=0.25
#z=42,Mo atom
#This program is for projected potential in 1d
pi=3.14
r=np.sqrt(x**2+y**2)
a1=6.10160120*10**-1
b1=9.11628054*10**-2
a2=1.26544000
b2=5.06776025*10**-1
a3=1.97428762
b3=5.89590381
c1=6.48028962*10**-1
d1=1.46634108
c2=2.60380817*10**-3
d2=7.84336311*10**-3
c3=1.13887493*10**-1
d3=1.55114340*10**-1
#Z= 6, chisq= 0.102440
#v=4*pi**2*0.529*14.4*spl.j0(2*pi*r*np.sqrt(b1)*a1)+2*pi**2*0.529*14.4*(c1/d1)*np.exp(-pi**2*r**2/d1)+4*pi**2*0.529*14.4*spl.j0(2*pi*r*np.sqrt(b2)*a1)+2*pi**2*0.529*14.4*(c2/d2)*np.exp(-pi**2*r**2/d2)+4*pi**2*0.529*14.4*spl.j0(2*pi*r*np.sqrt(b3)*a3)+2*pi**2*0.529*14.4*(c3/d3)*np.exp(-pi**2*r**2/d3)
#v=4*pi**2*0.529*14.4*(a1*spl.k0(2*pi*r*np.sqrt(b1))+a2*spl.k0(2*pi*r*np.sqrt(b2))+a3*spl.k0(2*pi*r*np.sqrt(b3)))+2*pi**2*0.529*14.4*((c1/d1)*np.exp(-(pi**2*r**2/d1))+(c2/d2)*np.exp(-(pi**2*r**2/d2))+(c3/d3)*np.exp(-(pi**2*r**2/d3)))

for m in range (482,542,20):
    for n in range(482,542,20):

        for ix in range (0,20):
            for jy in range (0,20):
                for g1 in range(-400,486,60):
                    for g2 in range(-400,486,60):
                        #print([n+jy+g2])
                       v[m+ix+g1,n+jy+g2]=np.exp(-r[m+ix,n+jy]**2/sigma**2)
plt.imshow(v)
#plt.imshow(z)
c=(fftim.fft2(v))
d=fftim.fftshift(c)
plt.figure()
plt.imshow((np.abs(d)))
plt.show()



