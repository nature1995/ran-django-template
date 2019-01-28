from django.shortcuts import render,  render_to_response
from apps.gallery.models import Gallery


def home(request):
    gallerys = Gallery.objects
    return render(request, 'home.html', {'gallerys': gallerys})


def game_2048(request):
    return render(request, '2048.html')


def game_snake(request):
    return render(request, 'snake.html')


def baidu_cloud(request):
    return render(request, 'baidu_cloud.html')


def page_not_found(request):
    return render_to_response('404.html')


def page_error(request):
    return render_to_response('500.html')








