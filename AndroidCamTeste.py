import urllib.request
import cv2
import numpy as np
import time

URL = "http://10.2.21.51:8080/"
while True:
    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
    img = cv2.imdecode(img_arr,-1)
    cv2.imshow('IPWebcam',img)
    
    if cv2.waitKey(1):
        break