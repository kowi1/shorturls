from rest_framework import serializers
from django.contrib.auth.models import User
from shorturls.models import UrlEntry

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = User
         fields =('url','username','email','is_staff','password')
        

class RediretUrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = UrlEntry
         fields =('origin_domain','short_url','friendly_name')

class GetShortUrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = UrlEntry
         fields =('origin_domain','short_url')
         
class GetFriendlyNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = UrlEntry
         fields =('friendly_name')