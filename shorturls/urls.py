"""shorturls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url,include

from shorturls.baseconv import base62
from shorturls.routers import router
from shorturls.viewset import EntryViewSet


print(base62.from_decimal(12345))

urlpatterns = [
     path('admin/', admin.site.urls),
    # path('A/<slug:title>/',  admin.site.urls),

     url(r'^', include(router.urls)),
     url(r'^api_auth/', include('rest_framework.urls',namespace='rest_framework'))
     # path('api_auth/', admin.site.urls),
     # path('shorturl/', include('shorturls.urls')),
]
