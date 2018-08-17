"""xiawu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from app01 import views as v1
from app02 import views as v2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^app01/login/$', v1.login),
    url(r'^app01/home/$', v1.home),
    url(r'^app01/logout/$', v1.logout),
    url(r'^app01/index/$', v1.index),

    url(r'^app02/login/$', v2.login),
    url(r'^app02/home/$', v2.home),
    url(r'^app02/logout/$', v2.logout),
    url(r'^app02/index/$', v2.index),
]
