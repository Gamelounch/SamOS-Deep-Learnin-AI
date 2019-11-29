import cv2
import numpy as np
import matplotlib.pyplot as plt

#                                0
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

cv2.imshow('image', img)
cv2.waitkey(0)
cv2.destroyallwindows()
