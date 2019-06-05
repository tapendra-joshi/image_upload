from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.http import HttpResponse
from django.conf import settings
#from wsgiref.util import FileWrapper
from django.core.files import File as FileWrapper
import mimetypes
import os


def img_view(request):
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImgForm()
    pics = Img.objects.all()

    return render(request, 'upload_img.html', {'form': form, 'pics': pics})


def img_list(request):
    total_imgs = Img.objects.all()
    return render(request, 'img_list.html', {'total_imgs': total_imgs})


def download(request, img_name):
    f = get_object_or_404(Img, name=img_name)
    img_path = settings.MEDIA_ROOT+'/images' + img_name
    img_wrapper = FileWrapper(f.img)
    content_type = mimetypes.guess_type(f.img)
    response = HttpResponse(img_wrapper, content_type=content_type)
    response['X-Sendfile'] = img_path
    response['Content-Disposition'] = 'attachment; filename=%s' % f.name
    response['Content-Length'] = os.stat(img_path).st_size

    return response


def success(request):
    return HttpResponse('successfully uploaded')
