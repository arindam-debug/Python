#This program is for periodic circular aperture
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fftim
z=np.zeros(1048576).reshape(1024,1024)
z1=np.zeros(1048576).reshape(1024,1024)
X=np.zeros(1048576).reshape(1024,1024)
Y=np.zeros(1048576).reshape(1024,1024)
def create_circular_mask(h=1024, w=1024, center=None):

    if center is None: # use the middle of the image
        center = [int(w/2), int(h/2)]
    #if radius is None: # use the smallest distance between the center and image walls
        #radius = min(center[0], center[0], w-center[0], h-center[0])

    X, Y= np.ogrid[:h,:w]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[0])**2)

    mask = dist_from_center >= 30
    return mask
z=z+create_circular_mask()
for m in range (482,542,20):
    for n in range(482,542,20):

        for ix in range (0,20):
            for jy in range (0,20):
                for g1 in range(-400,486,60):
                    for g2 in range(-400,486,60):
                        #print([n+jy+g2])
                       z1[m+ix+g1,n+jy+g2]=z[m+ix,n+jy]
plt.figure()
plt.imshow(z1), plt.title('ap')
c=(fftim.fft2(z1))
d=fftim.fftshift(c)
w=np.abs(d)
plt.figure()
plt.imshow(w), plt.title('FFT')
plt.show()
