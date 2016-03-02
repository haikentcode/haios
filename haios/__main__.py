#!/usr/bin/env python
from descriptor import descriptor as des
from distance import distance as dis
from spider import spider
from objects import objects
import sys
import cv2
import threading
import time
import random

def hkresize(image):
    r=100.0/image.shape[1]
    dim=(100,int(image.shape[0]*r))
    resize=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
    return resize

def hkimshow(title,image):
        r=200.0/image.shape[1]
        dim=(200,int(image.shape[0]*r))
        resize=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
        cv2.imshow(title,resize)

dirs=("/home/haikent/Pictures/lalla",) #'/media/haikent/521686E01686C487/picture/'

class matching(threading.Thread):
      key={}
      result=[]
      def __init__(self,image):
          threading.Thread.__init__(self)
          self.image=image

      def run(self):
           try:
               img=cv2.imread(self.image)
               img=hkresize(img)
               cd=des.ColorDescriptor((8,12,3))
               f1=self.key["cd"]
               f2=cd.describe(img)
               distance=dis.Distance(f1,f2)
               """faceObj=objects.Face()
               faceList=faceObj.getFaces(img)"""
               fd=1
               """for face1 in self.key["faces"]:
                   for face2 in faceList:
                       lbp=des.LBPDescriptor(3)
                       ff1=lbp.describe(face1)
                       ff2=lbp.describe(face2)
                       facedistance=dis.Distance(ff1,ff2)
                       if facedistance.chi_distance() < 0.009 :
                               fd+=1
               #if fd > 1 :
                #    hkimshow(str(distance.chi_distance()),img)"""
               print distance.chi_distance(),fd
               self.result.append((self.image,distance.chi_distance(),1.0/fd))
           except:
               print "error",self.image


def desktopSearch(imgp):
       image = cv2.imread(imgp)
       image = hkresize(image)
       cd=des.ColorDescriptor((8,12,3))
       matching.key["cd"]=cd.describe(image)

       faceObj=objects.Face()
       matching.key["faces"]=faceObj.getFaces(image)
       imlist=[]
       for dir in dirs:
           imlist+=spider.desktopSpiderThread(dir)
       print imlist
       thrdlist=[]
       print "scaning...."
       i=0
       for img in imlist:
           th=matching(img)
           thrdlist.append(th)
           th.start()
           time.sleep(0.01)

       for  th in thrdlist:
           th.join()
       print "complete scan"
       cv2.waitKey(0)
       cv2.destroyAllWindows()
       print matching.result


def main():
    if len(sys.argv) > 1:
            desktopSearch(sys.argv[1])
            #print cv2.imread("haios/image/smile.jpg")
    else:
        print "please provide image path"

if __name__ == '__main__':
    main()
