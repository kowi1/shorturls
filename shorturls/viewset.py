from rest_framework import  viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from shorturls.models import UrlEntry
from rest_framework.decorators import action
from rest_framework import permissions
from django.http import HttpResponse,HttpResponseRedirect

from shorturls.serializer import UserSerializer,GetShortUrlSerializer,GetFriendlyNameSerializer

class UserInputViewSet (viewsets.ModelViewSet):
        queryset = User.objects.all()
        serializer_class = UserSerializer

class UserViewSet (viewsets.ViewSet):
     

     def list(self,request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True,context={'request':request})
        return Response(serializer.data)

     def retrieve(self,request,pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset,pk=pk)
        serializer = UserSerializer(user,context={'request':request})
        return Response(serializer.data)

     def get_serializer_context(self):
        context = super(UserViewSet,self).get_serializer_context()
        return context
     
      

class GetShortUrlViewSet (viewsets.ViewSet):
     

     def list(self,request):
         queryset = UrlEntry.objects.all()
         serializer = GetShortUrlSerializer(queryset, many=True,context={'request':request})
         return Response(serializer.data)
        
     def retrieve(self,request,pk=None):
         queryset = UrlEntry.objects.all()
         user = get_object_or_404(queryset,pk=pk)
         serializer = GetShortUrlSerializer(user,context={'request':request})
         return Response(serializer.data)

     



class GetFriendlyNameViewSet (viewsets.ViewSet):
     

     def list(self,request):
         queryset = UrlEntry.objects.all()
         serializer = GetFriendlyNameSerializer(queryset, many=True,context={'request':request})
         return Response(serializer.data)
        
     def retrieve(self,request,pk=None):
         queryset = UrlEntry.objects.all()
         user = get_object_or_404(queryset,pk=pk)
         serializer = GetFriendlyNameSerializer(user,context={'request':request})
         return Response(serializer.data)

class EntryViewSet(viewsets.ModelViewSet):
         queryset = UrlEntry.objects.all()
         serializer_class=GetShortUrlSerializer
         permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
         def create(self,request,*args,**kwargs):
                 response = super(EntryViewSet,self).create(request,*args,**kwargs)
                 return HttpResponseRedirect(redirect_to='https:google.com')
         def perform_create(self,serializer):
                 serializer.partial=True
                 serializer.save( origin_ip=self.request.META.get('REMOTE_ADDR'))