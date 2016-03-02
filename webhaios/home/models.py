from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from datetime import datetime
from string import join
import os
import uuid

Image_Folder="profilePic/"
class Student(models.Model):
       name=models.CharField(max_length=100)
       gender=models.CharField(max_length=5)
       contactNo=models.CharField(max_length=10)
       image=models.ImageField(upload_to=Image_Folder) #pip install Pillow
