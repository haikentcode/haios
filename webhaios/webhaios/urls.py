"""webhaios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import home
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$','home.views.index',name='home'),
    url(r'^gettime/','home.views.gettime',name='gettime'),
    url(r'^calculate/','home.views.calculate',name='calculate'),
    url(r'^upload/','home.views.upload',name='upload'),
    url(r'^studentform/','home.views.StudentForm',name='studentform')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
