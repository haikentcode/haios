"""
@ Dec 2015 HAIOS PRODUCT ( haikent < hitesh kumar regar> )

"""

#open cv
import cv2
#open cv
import cv

# for storing image in arrya
import numpy as np

# Local Binary Pattern function
from skimage.feature import local_binary_pattern as LBP
# To calculate a normalized histogram
from scipy.stats import itemfreq

"""
ABOUT LBP Descriptor -- @source:http://hanzratech.in/2015/05/30/local-binary-patterns.html
=======STEP=====
1. Load the color image.
2. Convert to grayscale image.
3. Calculate the LBP mask.
4. Calculate the LBP Histogram and normalize it.
"""

class LBPDescriptor:
    def __init__(self,radius=3):
        self.radius = radius

    def describe(self,image):
        #convert the image to the hsv color space and initialize
        #the features used to quantify the image
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        # Number of points to be considered as neighbourers
        points = 8 * self.radius

        lbp=LBP(image,points,self.radius,method='uniform')
        x = itemfreq(lbp . ravel())
        # Normalize the histogram
        hist = x[:, 1] / sum(x[:, 1])
        return hist


class ColorDescriptor:
        def __init__(self,bins):
                   #store the no of bins for 3d histogram
                self.bins=bins
        def histogram(self, image, mask):
                # extract a 3D color histogram from the masked region of the
                # image, using the supplied number of bins per channel; then
                # normalize the histogram
                try:
                   hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins,[0, 180, 0, 256, 0, 256])
                except :
                   print "exception"
                   hist=0
                hist = cv2.normalize(hist).flatten()
                # return the histogram
                return hist
        def describe(self,image):
             #convert the image to the hsv color space and initialize
             #the features used to quantify the image
             image = cv2.cvtColor(image,cv.CV_BGR2HSV)
             features = []

             #grab the dimension and compute the center of the image
             (h,w) = image.shape[:2]
             (cX,cY) = (int(w*0.5),int(h*0.5))

             #devide the image into four rectangles /
             #segments (top-left,top-right,bottom-right,bottom-left)

             segments = [(0,cX,0,cY),(cX,w,0,cY),(cX,w,cY,h),(0,cX,cY,h)]

             #costruct an elliptical mask representing the center of the image
             (axesX,axesY) = (int(w*0.75)/2,int(h*0.75)/2)
             ellipsMask = np.zeros(image.shape[:2],dtype="uint8")
             cv2.ellipse(ellipsMask,(cX,cY),(axesX,axesY),0,0,360,255,-1)

             # Loop over the segments
             for (startX,endX,startY,endY) in segments:
                 #construct a mask for each corner of the images , subtracting
                 #the ellipticalcenter from it
                 cornerMask = np.zeros(image.shape[:2],dtype="uint8")
                 cv2.rectangle(cornerMask,(startX,startY),(endX,endY),255,-1)
                 cornerMask=cv2.subtract(cornerMask,ellipsMask)

                 #extract a color histogram from the elliptical region and
                 #update the frature vector

                 hist = self.histogram(image,ellipsMask)
                 features.extend(hist)

             #return the feature vector
             return features

def hello():
        return "your are in  descriptor module"
