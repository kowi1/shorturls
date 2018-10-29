from rest_framework import serializers
from django.contrib.auth.models import User
from shorturls.models import UrlEntry


        

class RedirectUrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = UrlEntry
         fields =('origin_domain','short_url','friendly_name')
         
class FullEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = UrlEntry
         fields =('id','origin_domain','short_url','friendly_name','origin_ip','views','friendly_key')

class GetShortUrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = UrlEntry
         fields =('origin_domain','short_url')
         read_only_fields=('short_url',)
         lookup_field='friendly_name'
         extra_kwargs={
             'url':{'lookup_field':'friendly_name'}
         }

class GetFriendlyNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = UrlEntry
         fields =('origin_domain','friendly_name','friendly_key')
         read_only_fields=('friendly_key',)
         lookup_field='friendly_key'
         extra_kwargs={
             'url':{'lookup_field':'friendly_key'}
         }
class OriginUrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = UrlEntry
         fields =('origin_domain',)
         lookup_field='friendly_name'
         extra_kwargs={
             'url':{'lookup_field':'friendly_name'}
         }
