# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:19:25 2020

@author: zcnay
"""

import matplotlib.pyplot as plt
import numpy as np
image = plt.imread('Purdue_Arch.png')
out = np.zeros((image.shape[0], image.shape[1],3))
heightCounter = 0
for height in image:
    widthCounter = 0
    for width in height:
        luminosity =  0.2126*image[heightCounter][widthCounter][0] + 0.7152*image[heightCounter][widthCounter][1] + 0.0722*image[heightCounter][widthCounter][2]
        out[heightCounter][widthCounter][0] = luminosity
        out[heightCounter][widthCounter][1] = luminosity
        out[heightCounter][widthCounter][2] = luminosity
        widthCounter += 1
    heightCounter += 1
plt.imsave('output.png', out)
