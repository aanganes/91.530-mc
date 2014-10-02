__author__ = 'tmlewis'
import cv2
import config

def read_file(path):
    if config.verbose:
        print 'Reading in image: ' + str(path)

#TODO check if file exists before reading
    img = cv2.imread(path,0)
    return [img]

