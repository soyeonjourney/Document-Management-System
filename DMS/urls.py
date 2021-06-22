"""DMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings
from users.views import ActiveUser


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='getstarted.html'), name='get-started'),
    path('home', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
    # Users (login, register, logout, ...)
    path('user/', include('users.urls')),
    re_path('active/(?P<active_code>.*)/', ActiveUser.as_view(), name='user-active'),
    # Library (allcvs, cvpr2020, ...)
    path('library/', include('library.urls')),
    # Statistics
    path('stats/', include('stats.urls')),
    # Collections
    path('collection/', include('collection.urls')),

    # Load static files
    re_path('static/(?P<path>.*)', serve,
        {'document_root': settings.STATIC_ROOT}, name='static'),
]
