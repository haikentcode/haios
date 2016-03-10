# haios [ ###image search engine ]


###how to use
```python
#for local data
1.store the sample images at location "/haios/webhaios/media/sampleData"
2.now you have installed Open-CV and Django in your system
3.go to location /haios/webhaios/ 
4.start the server using command "python manage.py runserver"
5.now application run on "https://localhost:8000" open in browser
6.now upload image to find similar image
#for online data
 ........comming soon
 
````



````python
   haios/
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
Image Search Engine (Final Year Project)
