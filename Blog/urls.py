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
from apps.blog import views as ablog

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', home, name='main'),
    path(r'blogs/', include('apps.blogs.urls'), ),
    path(r'accounts/', include('allauth.urls')),
    path(r'accounts/', include('myauth.urls')),
    # path(r'account/', include('account.urls')),
    path('blog/', ablog.ablog, name='ablog'),
    path('articles/<int:id>/', ablog.detail, name='detail'),
    path('category/<int:id>/', ablog.search_category, name='category_menu'),
    path('tag/<str:tag>/', ablog.search_tag, name='search_tag'),
    path('archives/<str:year>/<str:month>', ablog.archives, name='archives'),
    path('summernote/', include('django_summernote.urls')),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^favicon.ico$', RedirectView.as_view(url=r'media/favicon.ico')),
    url(r'^qr/(.+)$', generate_qrcode, name='qr'),
    url(r'^qr/', home, name='qrcode'),
    url(r'^baidu_cloud/', baidu_cloud, name='baidu_cloud'),
    path(r'iot/', include('apps.myapp.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,) + static(settings.STATIC_URL,
                                                                            document_root=settings.STATIC_ROOT)
