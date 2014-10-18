import getopt
import sys
from matplotlib import pyplot as plt
import imageReader
import imageProces
from imageViewer import imageViewer
import numpy as np
import os
import cv2

from PyQt4 import QtCore, QtGui

import config


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "vho:f:d:r")
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)
    if argv.__len__() <= 1:
        usage()
        sys.exit(2)

    for o, a in opts:
        if o == "-v":
            print 'verbose mode'
            config.verbose = True
        if o == "-r":
            config.render = True
        if o == "-f":
            imageDic = imageReader.read_file(a)
        if o == "-o":
            print 'output directiory is set to ' + str(a)
            config.write_out=True
            config.output_dir = str(a)
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-d"):
            imageDic = imageReader.read_directory(a)


    print 'Processing ' + str(imageDic.__len__()) + ' images'
    for key in imageDic.keys():
        image = imageDic[key]
        processedImage = imageProces.process_image(image)
        #imageDic[key] = cv2.add(image,processedImage)
        imageDic[key] = processedImage

    if config.write_out:
        if config.verbose:
            print 'writing images to disk'
            print 'checking to see if output directory exists'
        dir = os.path.dirname(__file__)
        output_path = os.path.join(dir, config.output_dir)
        if os.path.exists(output_path):
            if config.verbose:
                print 'it does'
        else:
            if config.verbose:
                print 'it does not'
            os.makedirs(output_path)
            if config.verbose:
                print 'Created output Path'
        for key in imageDic.keys():
            path, filename = os.path.split(key)
            cv2.imwrite(os.path.join(config.output_dir,filename),imageDic[key])



#    if config.render:
#        render_image_on_screen(imageDic[0])


def render_image_on_screen(processedImages):
    if config.verbose:
        print 'attempting to render'
    app = QtGui.QApplication(sys.argv)
    myimageViewer = imageViewer()
    myimageViewer.setDefaults(processedImages[1])
    myimageViewer.show()
    sys.exit(app.exec_())




def usage():
    print '<name>.py -f <inputfile>  to process a file'
    print '<name>.py -v to increase debugging output'
    print '<name>.py -d to process a directory full of images'

if __name__ == '__main__':   main(sys.argv[1:])