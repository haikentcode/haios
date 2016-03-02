from django.shortcuts import render,HttpResponse,render_to_response

"""
from django.shortcuts import
Http404                        _dirs_undefined
HttpResponse                   _get_queryset
HttpResponsePermanentRedirect  force_text
HttpResponseRedirect           get_list_or_404
Manager                        get_object_or_404
ModelBase                      loader
Promise                        redirect
QuerySet                       render
RemovedInDjango110Warning      render_to_response
RequestContext                 resolve_url
_context_instance_undefined    six
_current_app_undefined         urlresolvers
_dictionary_undefined          warnings

"""
from django.views.decorators.csrf import csrf_exempt
from froms import FeedBack,Student
import datetime
import time

#haios package
from descriptor import descriptor as des
from distance import distance as dis
from spider import spider
from objects import objects
import sys
import cv2


def handle_uploaded_file(f,name):
    ext=str(name.split(".").pop())
    name=str(time.time()).replace(".","")
    imagePath='media/'+name+"."+ext
    with open(imagePath, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return imagePath

def getSimilarImages(imagePath): # pass image path to get list of similar images path and urls
       imagesList=[]
       for i in range(100):
           imagesList.append(imagePath)
       return imagesList

@csrf_exempt
def upload(request):
    f=request.FILES['file']
    name=f.name
    imagePath=handle_uploaded_file(f,name)
    print imagePath
    similarImagesList=getSimilarImages(imagePath)
    return render(request,'home/imageslist.html',{"similarImagesList":similarImagesList}) #get templet of list of images


def index(request):
    if request.method == 'POST':
        form = FeedBack(request.POST)
        if form.is_valid():
           print request.POST.get('topic')
           return render(request,'home/index.html',{"name":"HAIOS","feedBackForm":form})
    print request
    feedBackForm=FeedBack()
    return render(request,'home/index.html',{"name":"HAIOS","feedBackForm":feedBackForm})
