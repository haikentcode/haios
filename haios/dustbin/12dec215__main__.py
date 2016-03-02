#!/usr/bin/env python
from descriptor import descriptor as des
from distance import distance as dis
from spider import spider
from objects import objects
import sys
import cv2

def set(image):
    # set image descriptor in database return type True / False
    print "demo"
    return True

def get(imageA):
    #def similar image from database return type image list with comp %
    filelist = runSpider()
    filelist = [x for x in filelist if x.endswith(".jpg")] # dir image list
    matchList = []
    fal=getFace(imageA)
    for imageB in filelist:
        d = compare(imageA,imageB)
        fbl=getFace(imageB)
        fd=[]
        for i in range(len(fal)):
            for j in range(len(fbl)):
                x=compareFace(fal[i],fbl[j])
                if x < 0.001:
                     fd.append(x)
        fd.sort()
        print d
        print fd
        if d < 11:
            matchList.append((imageB,d,))
    matchList.sort()
    return len(matchList)

def compare(imageA,imageB):
    imgA = cv2.imread(imageA)
    imgB = cv2.imread(imageB)
    hk=False
    if hk:
       feature = des.LBPDescriptor(3)
    else:
       feature = des.ColorDescriptor((8,12,3))
    f1 = feature.describe(imgA)
    f2 = feature.describe(imgB)

    distance = dis.Distance(f1,f2)

    return distance.chi_distance()

def compareFace(faceA,faceB):
    feature = des.LBPDescriptor(3)
    fa=feature.describe(faceA)
    fb=feature.describe(faceB)
    distance = dis.Distance(fa,fb)
    return distance.chi_distance()


def runSpider():
      dspid = spider.DesktopSpider()
      dspid.run()
      return dspid.filelist

def showAllFaces():
      imagesList=runSpider()
      i=0
      for image in imagesList:
          if i > 50 :
              break
          faces=getFace(image)
          for face in faces:
              cv2.imshow(str(i),face)
              i+=1
      cv2.waitKey(0)
      cv2.destroyAllWindows()

def getFace(imagePath):
    image = cv2.imread(imagePath)
    faceImagesObject=objects.Face() # Create Face class Object
    faceImages = faceImagesObject.getFaces(image) # return all faces image list
    return faceImages

    """
    for i in range(len(faceImages)):
        for j in range(i+1,len(faceImages)):
             print "compare",i,"to",j,"=",compareFace(faceImages[i],faceImages[j])
    i=0
    for image in faceImages:
         cv2.imshow('img'+str(i),image)
         i+=1
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """


def help():
    print "COMMAND ARGUMENT -- DISCRIPTION"
    print "set imagePath -- for put image in database"
    print "get imagePath -- for get similar imgage from database"
    print "compare imageApathe imageBpathe -- for compare two image"
    print "runSpider  -- for index folder image with "
    print "getFace imagePath -- for getting faces from image"

def main():
    #deal with passing command in arguent for __main__.py
      if len(sys.argv) >1:
          if sys.argv[1] == "set":
               return set(sys.argv[2])
          elif sys.argv[1] == "get":
               return get(sys.argv[2])
          elif sys.argv[1] == "compare" and len(sys.argv)>3:
               return compare(sys.argv[2],sys.argv[3])
          elif sys.argv[1] == "getFace" and len(sys.argv)>2 :
               return getFace(sys.argv[2])
          elif sys.argv[1] == "runSpider":
               return runSpider()
          elif sys.argv[1] == "showAllFaces" :
            return showAllFaces()
          else:
              help()
      else:
           help()

if __name__ == "__main__":
        r=main()
        print r
