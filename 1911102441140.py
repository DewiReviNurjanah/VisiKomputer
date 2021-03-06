# -*- coding: utf-8 -*-
"""1911102441140.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vd1GX3WDXtinF2_paDXTlZ-bEJPRUYeS

**Dewi Revi Nurjanah - 1911102441140**
"""

from google.colab import files
import cv2
file = files.upload()

!ls
from google.colab.patches import cv2_imshow
img = cv2.imread('smartcity.jpg')
cv2_imshow(img)

from matplotlib import pyplot as plt

fig = plt.figure()
fig.add_subplot(121)

plt.imshow(img)

fig.add_subplot(122)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img2)

plt.show()

# Commented out IPython magic to ensure Python compatibility.
import cv2
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
img = cv2.imread('smartcity.jpg')
width, height = img.shape[:2]
R = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
img_rotation = cv2.warpAffine(img, R, (width, height))
plt.imshow(img_rotation)

img = cv2.imread("smartcity.jpg")[:, :, ::-1]
fig, axes = plt.subplots(2, 2, figsize = (8, 8))

fig.tight_layout()

axes = axes.ravel()
axes[0].imshow(img)
axes[1].imshow(img[:, ::-1, :])
axes[2].imshow(img[::-1, :, :])
axes[3].imshow(img[::-1, ::-1, :])