__author__ = 'tmlewis'

import cv2
import config

def process_image(image):
    if config.verbose:
        print 'running on image with edge algo'
    #edges = cv2.Canny(image, 100, 200)
    surf = cv2.SURF(400)
    kp, des = surf.detectAndCompute(image,None)
    edges = cv2.drawKeypoints(image,kp,None,(255,0,0),4)

    return edges
