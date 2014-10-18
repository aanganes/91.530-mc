__author__ = 'tmlewis'
import cv2
import config
import os
import os

def read_file(path):
    if config.verbose:
        print 'Reading in image: ' + str(path)

#TODO check if file exists before reading
    img = cv2.imread(path,0)
    return {path:img}


def read_directory(path):
    imageList ={}
    dir = os.path.dirname(__file__)
    path_name = os.path.join(dir, path)
    for (dirpath, dirnames, filenames) in os.walk(path_name):

        if config.verbose:
            print 'Running directory of ' + str(path)
            print 'files are '+ str(filenames)
            print os.listdir(path)

        break
    for filename in filenames:
        if filename.startswith("."):
            continue
        readImage = read_file(os.path.join(path_name,filename))
        # need to strip it out of a list
        for entry in readImage.keys():
         imageList[entry] = readImage[entry]




    return imageList
