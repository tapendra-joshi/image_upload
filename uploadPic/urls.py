from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

    url('', views.img_list, name='list'),
    url('upload', views.img_view, name='image_upload'),
    url('success', views.success, name='success'),
    url(r'^download/(?P<img_name>.+)$', views.download, name='download'),


]