from rest_framework import routers
from shorturls.viewset import ViewUrlViewSet,GetShortUrlViewSet,GetFriendlyNameViewSet,EntryViewSet


router = routers.DefaultRouter()

router.register(r'getshorturl',GetShortUrlViewSet,basename='getshorturl')
router.register(r'redirect',EntryViewSet,basename='entry')
router.register(r'friendlyname',GetFriendlyNameViewSet,basename='friendentry')
router.register(r'fullentry',ViewUrlViewSet,basename='fullentry')