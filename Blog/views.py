from django.shortcuts import render
from apps.gallery.models import Gallery


def home(request):
    gallerys = Gallery.objects
    return render(request, 'home.html', {'gallerys': gallerys})


def baidu_cloud(request):
    return render(request, 'baidu_cloud.html')


def handler404(request, exception):
    return render(request, template_name='404.html')


def handler500(request):
    return render(request, template_name='500.html')








