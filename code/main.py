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
    if argv.__len__() <= 1:
        usage()
        sys.exit(2)

    for o, a in opts:
        if o == "-v":
            config.verbose = True
        if o == "-f":
            imageList = imageReader.read_file(a)
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-d"):
            #imageList = imageReader.readDir(a)
            print 'Directories are not supported yet'
            sys.exit(2)

    for img in imageList:
        processedImages = imageProces.process_image(img)

    render_image_on_screen(processedImages)


def render_image_on_screen(processedImages):
    if config.verbose:
        print 'attempting to render'
    plt.imshow(processedImages)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.show()


def usage():
    print '<name>.py -f <inputfile>  to process a file'
    print '<name>.py -v to increase debugging output'
    print '<name>.py -d to process a directory full of images'

if __name__ == '__main__':   main(sys.argv[1:])