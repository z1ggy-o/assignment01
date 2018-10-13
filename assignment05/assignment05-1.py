import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from skimage import io, color
from skimage import exposure

file_image	= 'cau.jpg'

im_color 	= io.imread(file_image)
im_gray  	= color.rgb2gray(im_color)

ker 		= np.array([[0,0,0],[0,1,0],[0,0,0]]) 
im_conv		= signal.convolve2d(im_gray, ker, boundary='symm', mode='same') 

p1 = plt.subplot(2,2,1)
p1.set_title('color image')
plt.imshow(im_color)
plt.axis('off')

p2 = plt.subplot(2,2,2)
p2.set_title('gray image')
plt.imshow(im_gray, cmap='gray')
plt.axis('off')

p3 = plt.subplot(2,2,3)
p3.set_title('convolution kernel')
plt.imshow(ker, cmap='gray')
plt.axis('off')

p4 = plt.subplot(2,2,4)
p4.set_title('convolution result')
plt.imshow(im_conv, cmap='gray')
plt.axis('off')

plt.show()