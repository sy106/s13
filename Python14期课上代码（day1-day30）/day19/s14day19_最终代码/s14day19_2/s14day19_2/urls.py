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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cmdb/', include("app01.urls")),
    url(r'^monitor/', include("app02.urls")),

]

"""
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^asdfasdfasdf/(?P<nid>\d+)/(?P<uid>\d+)/', template.index, name='indexx'),
    url(r'^login/', template.login),
    # url(r'^home/', template.home),
    url(r'^home/', template.Home.as_view()),
    # url(r'^detail/', template.detail),
    # url(r'^detail-(\d+)-(\d+).html', template.detail),
    # url(r'^detail-(?P<nid>\d+)-(?P<uid>\d+).html', template.detail),
    url(r'^detail-(?P<nid>\d+).html', template.detail),
]
"""
