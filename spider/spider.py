import os
import collections
import sys
import re
import thread
import time


class DesktopSpider:
    def __init__(self):
            self.filelist=[] #contain list of images path  for give folder path

    def run(self,dir="/home/haikent/Pictures"): # method to start scanDir thread
        self.scanDir(dir)

    def scanDir(self,dir):
        for name in os.listdir(dir):
            try:
                path=os.path.join(dir,name)
                if os.path.isfile(path):
                    self.filelist.append(path)
                else:
                    thread.start_new_thread(scanDir,(path,))
            except:
                print "error in scanDir"
def hello():
    print "welcome to spider module"
