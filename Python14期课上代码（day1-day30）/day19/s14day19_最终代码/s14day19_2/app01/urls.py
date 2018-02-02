"""s14day19_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^login/', views.login),
    url(r'^index/', views.index),
    url(r'^user_info/', views.user_info),
    url(r'^user_group/', views.user_group),
    url(r'^groupdel-(?P<uid>\d+)/', views.group_del),
    url(r'^userdetail-(?P<nid>\d+)/', views.user_detail),
    url(r'^userdel-(?P<nid>\d+)/', views.user_del),
    url(r'^useredit-(?P<nid>\d+)/', views.user_edit),
    url(r'^groupedit-(?P<uid>\d+)/', views.group_edit),
    url(r'^orm/', views.orm),
]

