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
# Create your views here.

import datetime
import time
def handle_uploaded_file(f,name):
    ext=str(name.split(".").pop())
    name=str(time.time()).replace(".","")
    with open('media/'+name+"."+ext, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@csrf_exempt
def upload(request):
    f=request.FILES['file']
    name=f.name
    handle_uploaded_file(f,name)
    return HttpResponse("ho gya tera")


@csrf_exempt
def calculate(request):
    expr=request.POST.get("expr")
    r=eval(expr)
    return HttpResponse(r)

def gettime(request):
    t=str(datetime.datetime.utcnow()).split(".")[0]
    return HttpResponse(t)

@csrf_exempt
def StudentForm(request):
    if request.method == 'POST':
        form=Student(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print "save"
        else:
            print request.FILES.get('image')
    studentform=Student()
    return render(request,'home/student.html',{"form":studentform})


def index(request):
    if request.method == 'POST':
        form = FeedBack(request.POST)
        if form.is_valid():
           print request.POST.get('topic')
           return render(request,'home/index.html',{"name":"india","feedBackForm":form})
    print request
    feedBackForm=FeedBack()
    return render(request,'home/index.html',{"name":"india","feedBackForm":feedBackForm})
