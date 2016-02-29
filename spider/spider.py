import os
import collections
import sys
import re
import thread
import time
import threading

class DesktopSpider(threading.Thread):
    filelist=[] #contain list of images path  for give folder path
    threadList=[] #running thread list
    def __init__(self,dir):
        threading.Thread.__init__(self)
        self.dir=dir

    def run(self): # method to start scanDir thread
        self.scanDir()

    def scanDir(self):
        for name in os.listdir(self.dir):
            try:
                path=os.path.join(self.dir,name)
                if os.path.isfile(path):
                    if fileIsImage(path):
                         self.filelist.append(path)
                else:
                    th=DesktopSpider(path)
                    th.start()
                    self.threadList.append(th)
            except:
                print "error in scanDir"



def fileIsImage(file):
    imageEx=("jpg","png","JPG","jpeg","JPEG","PNG")
    if file.endswith(imageEx):
        return True
    else:
        return False

def desktopSpiderThread(dir):
    thrd=DesktopSpider(dir) # create DesktopSpider class thread
    DesktopSpider.threadList.append(thrd) # add thread to list
    thrd.start()  # first thread start
    for th in DesktopSpider.threadList: # wait untill alll thred copleted
                    th.join()
    imageList=DesktopSpider.filelist # get collected file list by spider
    return imageList


def hello():
    print "welcome to spider module"
