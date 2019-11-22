#This program is for projected potential,block some portion and see the fft with line-scan
import scipy.ndimage
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fftim
x0, y0 = 50, 256 # These are in _pixel_ coordinates!!
x1, y1 = 500, 256
num = 1000
X, Y = np.linspace(x0, x1, num), np.linspace(y0, y1, num)
z1=np.zeros(262144).reshape(512,512)
z2=np.zeros(262144).reshape(512,512)
z3=np.ones(262144).reshape(512,512)
X1=np.zeros(262144).reshape(512,512)
Y1=np.zeros(262144).reshape(512,512)

import scipy.special as spl
x=y=np.linspace(-1.5,1.5,512)
from scipy.interpolate import interp1d
#v=np.zeros(262144).reshape(512,512)
x,y=np.meshgrid(x,y)
#z=42,Mo atom
#This program is for projected potential in 2d
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
v=4*pi**2*0.529*14.4*(a1*spl.k0(2*pi*r*np.sqrt(b1))+a2*spl.k0(2*pi*r*np.sqrt(b2))+a3*spl.k0(2*pi*r*np.sqrt(b3)))+2*pi**2*0.529*14.4*((c1/d1)*np.exp(-(pi**2*r**2/d1))+(c2/d2)*np.exp(-(pi**2*r**2/d2))+(c3/d3)*np.exp(-(pi**2*r**2/d3)))

def create_circular_mask(h=512, w=512, center=None):

    if center is None: # use the middle of the image
        center = [int(w/2), int(h/2)]


    X1, Y1= np.ogrid[:h,:w]
    dist_from_center = np.sqrt((X1 - center[0])**2 + (Y1-center[0])**2)

    mask = dist_from_center <= 200
    return mask
z1=z1+create_circular_mask()
X2=np.zeros(262144).reshape(512,512)
Y2=np.zeros(262144).reshape(512,512)
def create_circular_mask(h=512, w=512, center=None):

    if center is None: # use the middle of the image
        center = [int(w/2), int(h/2)]
    #if radius is None: # use the smallest distance between the center and image walls
    #radius = min(center[0], center[0], w-center[0], h-center[0])

    X2, Y2= np.ogrid[:h,:w]
    dist_from_center = np.sqrt((X2 - center[0])**2 + (Y2-center[0])**2)

    mask = dist_from_center >=80
    return mask
z2=z2+create_circular_mask()
z=z1*v+z2*v-v

#z=1
#create_circular_mask()=1
plt.figure()
plt.imshow(z, cmap='gray'), plt.title('ap')
c=(fftim.fft2(z))
d=fftim.fftshift(c)
w=np.abs(d)
plt.figure('Abs FFT')
plt.imshow(w),plt.title('Abs FFT')
zi = scipy.ndimage.map_coordinates(w, np.vstack((X,Y)))
fig, axes = plt.subplots(nrows=2)
axes[0].imshow(w)

axes[0].imshow(w)
axes[0].plot([x0, x1], [y0, y1], 'ro-')
axes[0].axis('image')

axes[1].plot(zi)
#plt.axis('off')
# #plt.colorbar()
plt.show()

