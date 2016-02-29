import numpy as np
import cv2

def hello():
    print "You are In Objects package"

class Text:
     'Find Text In Image and Convrt into Text'
     pass


class Face:
    'Extracting Face From Image'
    def __init__(self,scaleFactor=1.2,minNeighbors=5,minh=80,minw=80):
        self.scaleFactor=scaleFactor
        self.minNeighbors=minNeighbors
        self.minh=minh
        self.minw=minw
    def getFaces(self,image): #return face images list from image
        gimage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        faceObj=cv2.CascadeClassifier('haios/objects/xmldata/haarcascade_frontalface_default.xml')
        return self.getData(gimage,faceObj)

    def getSmileFaceByGRAY(self,gimage):
        faceObj=cv2.CascadeClassifier('haios/objects/xmldata/haarcascade_smile.xml')
        return self.getData(gimage,faceObj)

    def getSmileFace(self,image):
        gimage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        faceObj=cv2.CascadeClassifier('haios/objects/xmldata/haarcascade_smile.xml')
        return self.getData(gimage,faceObj)

    def getData(self,image,cascadeObj):
        faces = cascadeObj.detectMultiScale(image,self.scaleFactor,self.minNeighbors,minSize=(self.minh,self.minw)) #check
        faceImages=[]
        for (x,y,w,h) in faces:
            #crop image -> cropImage=image[y:y+w,x:x+h]
            cropImage=image[y:y+w,x:x+h]
            faceImages.append(cropImage)
        return faceImages    #  NOTE: return oringinal face not gray
