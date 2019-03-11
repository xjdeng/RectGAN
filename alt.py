import cv2
import numpy as np

def square(img, size = 64):
    if isinstance(img, str):
        img = cv2.imread(img)
    h,w,_ = img.shape
    d = max(h,w)
    img2 = 255*np.ones((d,d,3))
    if h > w:
        c = round((d-w)/2)
        img2[:,c:c+w,:] = img
    else:
        c = round((d-h)/2)
        img2[c:c+h,:,:] = img
    return cv2.resize(img2, (size, size))