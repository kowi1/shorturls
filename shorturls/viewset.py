from rest_framework import  viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from shorturls.models import UrlEntry
from rest_framework.decorators import action
from rest_framework import permissions
from django.http import HttpResponse,HttpResponseRedirect
from shorturls.baseconv import base62
from shorturls.settings import domain
from urllib.parse import urlparse
import os

from shorturls.serializer import GetShortUrlSerializer,FullEntrySerializer,GetFriendlyNameSerializer,OriginUrlSerializer

     
class GetShortUrlViewSet(viewsets.ModelViewSet):
         queryset = UrlEntry.objects.none()
         serializer_class=GetShortUrlSerializer
        
         def create(self,request):
                 queryset=UrlEntry.objects.create(OriginDomain=self.request.POST.get('OriginDomain'))
                 serializer = GetShortUrlSerializer(queryset,context={'request':request})
                 g=UrlEntry.objects.filter(pk=queryset.pk).update(ShortUrl=domain+base62.from_decimal(queryset.pk),FriendlyName=base62.from_decimal(queryset.pk),FriendlyKey=queryset.pk)
                 queryset.refresh_from_db()
                 return Response(serializer.data)
                 
class ViewUrlViewSet (viewsets.ViewSet):         
         def list(self,request):
                 queryset = UrlEntry.objects.all()
                 serializer = FullEntrySerializer(queryset, many=True,context={'request':request})
                 return Response(serializer.data)
        
         def retrieve(self,request,pk=None):
                 queryset = UrlEntry.objects.all()
                 user = get_object_or_404(queryset,pk=pk)
                 serializer = GetShortUrlSerializer(user,context={'request':request})
                 return Response(serializer.data)
     

class GetFriendlyNameViewSet (viewsets.ModelViewSet):
         queryset = UrlEntry.objects.none()
         serializer_class=GetFriendlyNameSerializer
         lookup_field = 'FriendlyKey'
         
         def perform_create(self,serializer):
                 queryset = UrlEntry.objects.all()
                 serializer.partial=True
                 serializer.save( FriendlyKey=base62.to_decimal(self.request.POST.get('FriendlyName')),ShortUrl=domain+self.request.POST.get('FriendlyName'))
                 return Response(serializer.data)


class OriginViewSet(viewsets.ViewSet):
         lookup_url_kwarg = 'FriendlyName'    
         def retrieve(self,request,*args, **kwargs):
                 queryset = UrlEntry.objects.all()
                 user = get_object_or_404(queryset,FriendlyName = kwargs['FriendlyName'] )
                 serializer = OriginUrlSerializer(user,context={'request':request})
                 g=UrlEntry.objects.filter(pk=user.pk).update(OriginIp=self.request.META.get('REMOTE_ADDR'),Views=UrlEntry.objects.get(pk=user.pk).Views+1)
                 return HttpResponseRedirect(redirect_to=user.OriginDomain)