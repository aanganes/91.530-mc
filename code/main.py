import getopt
import sys

from matplotlib import pyplot as plt

import imageReader
import imageProces
import config


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "vhf:d:")
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)
    if argv.__len__() <=1:
        usage()
        sys.exit(2)

    for o, a in opts:
        if o == "-v":
            config.verbose = True
        if o == "-f":
            imageList = imageReader.readFile(a)
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-d"):
            imageList = imageReader.readDir(a)
            print 'Directories are not supported yet'
            sys.exit(2)

    for img in imageList:
        processedImages = imageProces.proces(img)

    render(processedImages)


def render(processedImages):
    if config.verbose:
        print 'attempting to render'

        #sanity check below
        # import cv2
        # print sys.argv[3]
        # path = sys.argv[3]
        # import os.path
        # print str(os.path.isfile(sys.argv[3]))
        # processedImages = cv2.imread(sys.argv[3],0)


    plt.imshow(processedImages)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.show()

    im = array(Image.open('sample.jpg'))

def usage():
    print 'test.py -f <inputfile>  '

if __name__ == '__main__':   main(sys.argv[1:])