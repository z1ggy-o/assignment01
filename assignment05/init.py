# TODO
# define kernels for computing image gradients
# define kernels for smoothing image
# define any other kernel

# convolution
# kernel for computing the derivative in x-direction
# dernel for computing the derivative in y-direction
# function for computing the magnitude of the gradient
# function for computing the direction of the gradient

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from skimage import io, color
from skimage import exposure

file_image = 'cau.jpg'

im_color = io.imread(file_image)
im_gray = color.rgb2gray(im_color)

ker = np.array([
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]
               ])

im_conv = signal.convolve2d(im_gray, ker, boundary='symm', mode='same')

# define x-axis kernel
# kernel_x = np.array([1, 0, -1])
kernel_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])

# define y-axis kernel
# kernel_y = np.array([[1], [0], [-1]])
kernel_y = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

# define smooth kernel
kernel_smooth = np.array([
                          [1, 1, 1],
                          [1, 1, 1],
                          [1, 1, 1]
                         ]) / 9

# define sharpen kernel
kernel_sharpen = np.array([
                           [0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]
                          ])

# derivative functions
# derivative x-axis
de_x = signal.convolve2d(im_gray, kernel_x, boundary='symm', mode='same')

# derivative y-axis
de_y = signal.convolve2d(im_gray, kernel_y, boundary='symm', mode='same')

# absolute value of gradient
def gradient_abs(de_x, de_y):
    n_row = len(de_x)
    n_col = len(de_x[0])
    gd_x = []
    gd_y = []

    for i in range(n_row):
        for j in range(n_col):
            abs_x = abs(de_x[i][j])
            gd_x.append(abs_x)
            abs_y = abs(de_y[i][j])
            gd_y.append(abs_y)
    
    return (gd_x, gd_y)

# function for computing magnitude of the gradient
def magnitude(de_x, de_y):
    n_row = len(de_x)
    n_col = len(de_x[0])
    mag = np.empty([n_row, n_col])

    for i in range(n_row):
        for j in range(n_col):
            gradient = np.array([de_x[i][j], de_y[i][j]])
            dist = np.linalg.norm(gradient)
            mag[i][j] = dist

    return mag


# function for computing the direction of the gradient
def direction(de_x, de_y):
    n_row = len(de_x)
    n_col = len(de_x[0])
    direct = np.empty([n_row, n_col])

    for i in range(n_row):
        for j in range(n_col):
            gradient = np.array([de_x[i][j], de_y[i][j]])
            radius = np.arctan2(gradient[1], gradient[0])
            direct[i][j] = radius

    return direct

#
# plotting part
#
p1 = plt.subplot(3, 3, 1)
p1.set_title('color image')
plt.imshow(im_color)
plt.axis('off')

p2 = plt.subplot(3, 3, 2)
p2.set_title('gray image')
plt.imshow(im_gray, cmap='gray')
plt.axis('off')

p3 = plt.subplot(3, 3, 3)
p3.set_title('de x')
plt.imshow(de_x, cmap='gray')
plt.axis('off')

p4 = plt.subplot(3, 3, 4)
p4.set_title('de y')
plt.imshow(de_y, cmap='gray')
plt.axis('off')

mag = magnitude(de_x, de_y)
p5 = plt.subplot(3, 3, 5)
p5.set_title('magnitude')
plt.imshow(mag, cmap='gray')
plt.axis('off')

dirct = direction(de_x, de_y)
p6 = plt.subplot(3, 3, 6)
p6.set_title('direction')
plt.imshow(dirct, cmap='gray')
plt.axis('off')

smooth = signal.convolve2d(im_gray, kernel_smooth, boundary='symm', mode='same')
p6 = plt.subplot(3, 3, 7)
p6.set_title('smoothing')
plt.imshow(smooth, cmap='gray')
plt.axis('off')

sharpen = signal.convolve2d(im_gray, kernel_sharpen, boundary='symm', mode='same')
p6 = plt.subplot(3, 3, 8)
p6.set_title('sharpen')
plt.imshow(sharpen, cmap='gray')
plt.axis('off')

# gradients
g_x, g_y = gradient_abs(de_x, de_y)
plt.quiver(g_x, g_y)
plt.show()