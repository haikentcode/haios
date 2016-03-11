
from pymongo import MongoClient
from descriptor import descriptor as des
import os
import cv2
client = MongoClient()
db = client.haios
coll = db.sampleImages
cdObj=des.ColorDescriptor((8,12,3))
def fileIsImage(file):
    imageEx=("jpg","png","JPG","jpeg","JPEG","PNG")
    if file.endswith(imageEx):
        return True
    else:
        return False


for img in os.listdir("./sampleData/"):
    path=os.path.join("media/sampleData",img)
    if fileIsImage(path):
        image=cv2.imread(img)
        cd=unicode(cdObj.describe(image))
        id=coll.insert_one({"path":path,"cd":cd }).inserted_id
        print id
