# haios [ by haikent ]
< documentation last update 27Dec2015 8:24 by Hitesh>
haios

````python

    GUI:
      desktophaios(written BY Dikshant):

      webhaios(written By Haikent):
          #Django Application

    PACKAGE:
       descriptor (written By Haikent)
           class
             ColorDescriptor:(bins)
                    f:describe(image) return features of image

             LBPDescriptor:(radius)
                    f:describe(image) return features of image

       distance (written By Haikent)
          class
            Distance:(imageA,imageB) # input Image A feature and ImageB feature
                   f:chi_distance(EQS_VALUE) return distance b/w 2 img feature

       objects (written by Haikent)
           class
              Face:(scaleFactor=1.2,minNeighbors=5,minh=80,minw=80)
                f:getFaces(image) #return list of faces in image
           class
              Text:(comming soon....)

       spider (written by Haikent)
          class
             DesktopSpider:(dir)
                  ----thred class run as thread---
            f:desktopSpiderThread(dir) return the given dir's all images path list       
```
Final Year Project Image Search Engine ( Hitesh , Ashok , Dikshant ,Paras)
