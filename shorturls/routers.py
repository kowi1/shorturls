from rest_framework import routers
from shorturls.viewset import ViewUrlViewSet,GetShortUrlViewSet,GetFriendlyNameViewSet,OriginViewSet



class ApiDocumentView(routers.APIRootView):
  """ 
                 
    """""
class DoumentedRouter(routers.DefaultRouter):
    APIRootView = ApiDocumentView

router = DoumentedRouter()

router.register(r'getshorturl',GetShortUrlViewSet,'getshorturl')
router.register(r'r',OriginViewSet,'Redirect')
router.register(r'friendlyname',GetFriendlyNameViewSet,basename='friendlyentry')
router.register(r'fullentry',ViewUrlViewSet,basename='fullentry')