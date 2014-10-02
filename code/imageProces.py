__author__ = 'tmlewis'

import cv2
import config

def process_image(image):
    if config.verbose:
        print 'running on image with edge algo'
    edges = cv2.Canny(image, 50, 100)
    return edges
