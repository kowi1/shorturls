from rest_framework import serializers
from django.contrib.auth.models import User
from shorturls.models import UrlEntry

class RedirectUrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = UrlEntry
         fields =('OriginDomain','ShortUrl','FriendlyName')

         
         
class FullEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = UrlEntry
         fields =('id','OriginDomain','ShortUrl','FriendlyName','OriginIp','Views','FriendlyKey')


class GetShortUrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = UrlEntry
         fields =('OriginDomain','FriendlyName','ShortUrl')
         read_only_fields=('ShortUrl','FriendlyName')
         lookup_field='FriendlyName'
         extra_kwargs={
             'url':{'lookup_field':'FriendlyName'}
         }


class GetFriendlyNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = UrlEntry
         fields =('OriginDomain','ShortUrl','FriendlyName') 
         read_only_fields=('ShortUrl',)
         lookup_field='FriendlyKey'
         extra_kwargs={
             'url':{'lookup_field':'FriendlyKey'}
         }

class OriginUrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = UrlEntry
         read_only_fields=('OriginDomain',)
         fields =('OriginDomain',)
         lookup_field='FriendlyName'
         extra_kwargs={
             'url':{'lookup_field':'FriendlyName'}
         }
