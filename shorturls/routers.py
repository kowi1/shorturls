from rest_framework import routers
from shorturls.viewset import UserInputViewSet,ViewUrlViewSet,UserViewSet,GetShortUrlViewSet,GetFriendlyNameViewSet,EntryViewSet


router = routers.DefaultRouter()
router.register(r'users',UserViewSet,basename='user')
router.register(r'getshorturl',GetShortUrlViewSet,basename='getshorturl')
router.register(r'redirect',EntryViewSet,basename='entry')
router.register(r'UserInput',UserInputViewSet,basename='UserInput')
router.register(r'fullentry',ViewUrlViewSet,basename='fullentry')