import cv2

from matplotlib import pyplot as plt
#unbroken
#filename = '7978439.jpg'
#broken
filename = 'broken.jpeg'
img = cv2.imread(filename,0)
img2 = cv2.imread(filename,cv2.CV_LOAD_IMAGE_GRAYSCALE)
edges = cv2.Canny(img,50,100)
surf = cv2.SURF(85)
#cv2.cornerHarris(img2)
rad = 4
#gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
keypoints = surf.detect(img2)
for kp in keypoints:
        x = int(kp.pt[0])
        y = int(kp.pt[1])
        cv2.circle(img2, (x, y), rad, (0, 0, 255))


unbrokenFilename = '7978439.jpg'
img3 = cv2.imread(unbrokenFilename,0)
img4 = cv2.imread(unbrokenFilename,cv2.CV_LOAD_IMAGE_GRAYSCALE)
edges2 = cv2.Canny(img4,50,100)
surf = cv2.SURF(100)
for kp in keypoints:
        x = int(kp.pt[0])
        y = int(kp.pt[1])
        cv2.circle(img4, (x, y), rad, (0, 0, 255))

plt.subplot(231),plt.imshow(img,cmap = 'gray')
plt.title('Broken Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(edges,cmap = 'gray')
plt.title('Broken Edge Image'), plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(img2,cmap = 'gray')
plt.title("Broken Feature detection"), plt.xticks([]), plt.yticks([])

plt.subplot(234),plt.imshow(img3,cmap = 'gray')
plt.title('Unbroken Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(edges2,cmap = 'gray')
plt.title('Unbroken Edge Image'), plt.xticks([]), plt.yticks([])
plt.subplot(236),plt.imshow(img4,cmap = 'gray')
plt.title("Unbroken Feature detection"), plt.xticks([]), plt.yticks([])


plt.show()