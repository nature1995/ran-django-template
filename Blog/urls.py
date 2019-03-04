"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.conf.urls import url
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from apps.qrcreate.views import generate_qrcode
from django.views.static import serve
import Blog.views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', home, name='main'),
    path(r'blogs/', include('apps.blogs.urls'), ),
    path(r'accounts/', include('allauth.urls')),
    path(r'accounts/', include('myauth.urls')),
    # path(r'account/', include('account.urls')),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'media/favicon.ico')),
    url(r'^qr/(.+)$', generate_qrcode, name='qr'),
    url(r'^qr/', home, name='qrcode'),
    url(r'^2048/', game_2048, name='game_2048'),
    url(r'^snake/', game_snake, name='game_snake'),
    url(r'^baidu_cloud/', baidu_cloud, name='baidu_cloud'),
    path(r'iot/', include('apps.myapp.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,) + static(settings.STATIC_URL,
                                                                            document_root=settings.STATIC_ROOT)

handler404 = Blog.views.page_not_found
handler500 = Blog.views.page_error
