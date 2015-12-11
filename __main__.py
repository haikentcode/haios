#!/usr/bin/env python
from descriptor import descriptor as des
from distance import distance as dis
from spider import spider
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
    for imageB in filelist:
        d = compare(imageA,imageB)
        print d
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


def runSpider():
      dspid = spider.DesktopSpider()
      dspid.run()
      return dspid.filelist

def help():
    print "COMMAND ARGUMENT -- DISCRIPTION"
    print "set imagePath -- for put image in database"
    print "get imagePath -- for get similar imgage from database"
    print "compare imageApathe imageBpathe -- for compare two image"
    print "runSpider  -- for index folder image with "


def main():
    #deal with passing command in arguent for __main__.py
      if len(sys.argv) >1:
          if sys.argv[1] == "set":
               return set(sys.argv[2])
          elif sys.argv[1] == "get":
               return get(sys.argv[2])
          elif sys.argv[1] == "compare" and len(sys.argv)>3:
               return compare(sys.argv[2],sys.argv[3])
          elif sys.argv[1] == "runSpider":
               return runSpider()
          else:
              help()
      else:
           help()

if __name__ == "__main__":
        r=main()
        print r
