from rest_framework import routers
from shorturls.viewset import UserViewSet,UrlViewSet


router = routers.DefaultRouter()
router.register(r'users',UserViewSet,basename='user')
router.register(r'url',UrlViewSet,basename='url')