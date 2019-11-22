#This program is for periodic annular aperture and diffraction
#Dis. between two circle is 4 times than the outer radius
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fftim
z1=np.zeros(1048576).reshape(1024,1024)
z2=np.zeros(1048576).reshape(1024,1024)
z3=np.zeros(1048576).reshape(1024,1024)
z4=np.zeros(1048576).reshape(1024,1024)
z5=np.ones(1048576).reshape(1024,1024)
X1=np.zeros(1048576).reshape(1024,1024)
Y1=np.zeros(1048576).reshape(1024,1024)
def create_circular_mask(h=1024, w=1024, center=None):

    if center is None: # use the middle of the image
        center = [int(w/2), int(h/2)]


    X1, Y1= np.ogrid[:h,:w]
    dist_from_center = np.sqrt((X1 - center[0])**2 + (Y1-center[0])**2)

    mask = dist_from_center <= 15
    return mask
z1=z1+create_circular_mask()
X2=np.zeros(1048576).reshape(1024,1024)
Y2=np.zeros(1048576).reshape(1024,1024)
def create_circular_mask(h=1024, w=1024, center=None):

    if center is None: # use the middle of the image
        center = [int(w/2), int(h/2)]
    #if radius is None: # use the smallest distance between the center and image walls
    #radius = min(center[0], center[0], w-center[0], h-center[0])

    X2, Y2= np.ogrid[:h,:w]
    dist_from_center = np.sqrt((X2 - center[0])**2 + (Y2-center[0])**2)

    mask = dist_from_center >=10
    return mask
z2=z2+create_circular_mask()
z=z1+z2-z3
for m in range (482,542,20):
    for n in range(482,542,20):

        for ix in range (0,20):
            for jy in range (0,20):
                for g1 in range(-410,486,60):
                    for g2 in range(-410,486,60):
                        #print([n+jy+g2])
                       z4[m+ix+g1,n+jy+g2]=z[m+ix,n+jy]-z5[m+ix+g1,n+jy+g2]
#z=1
#create_circular_mask()=1
fig=plt.figure()
plt.imshow(z4, cmap='gray'), plt.title('ap')
#fig.savefig('plot.png')
c=(fftim.fft2(z4))
d=fftim.fftshift(c)
w=np.abs(d)
plt.figure()
plt.imshow(w, cmap='Blues_r'), plt.title('FFT')
plt.show()



