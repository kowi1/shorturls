from rest_framework import  viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from shorturls.models import UrlEntry
from shorturls.serializer import UserSerializer,UrlSerializer


class UserViewSet (viewsets.ViewSet):
    def list(self,request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset,pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

      

class UrlViewSet (viewsets.ModelViewSet):
     queryset = UrlEntry.objects.all()
     serializer_class = UrlSerializer 