#!/usr/bin/env python
from descriptor import descriptor as des
from distance import distance as dis
from spider import spider
from objects import objects
import sys
import cv2

sampleImage1=cv2.imread("./image/sampleImage1.jpg")
sampleImage2=cv2.imread("./image/sampleImage1.jpg")

def testSpider():
     dir="/home/haikent/Pictures/"
     return spider.desktopSpiderThread(dir)

def testDescriptor():
       lpbd=des.LBPDescriptor(3)
       cd=des.ColorDescriptor((8,12,3))
       return (lpbd.describe(sampleImage1),cd.describe(sampleImage1))


def testDistance():
      cd=des.ColorDescriptor((8,12,3))
      f1=cd.describe(sampleImage1)
      f2=cd.describe(sampleImage2)
      distance=dis.Distance(f1,f2)
      return distance.chi_distance()



def testObjects():
        faceObj=objects.Face(1.1,3,20,20) #1.1,3,20,20 #1.6,3,20,20
        sfaceObj=objects.Face(1.5,5,80,80) #1.5,20,40,40
        faceList=faceObj.getFaces(sampleImage1)
        smileFacelist=[]
        print faceObj
        for face in faceList:
            smileFacelist+=sfaceObj.getSmileFaceByGRAY(face)
        i=0
        for image in faceList:
            cv2.imshow(str(i),image)
            i+=1
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def main():
    funcList=[testDescriptor,testDistance , testSpider ,testObjects]
    if len(sys.argv) > 1 :
               test=sys.argv[1]
               for func in funcList:
                   if func.func_name == test :
                           return func()


if __name__ == "__main__" :
        r=main()
        print r
