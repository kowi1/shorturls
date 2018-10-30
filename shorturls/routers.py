from rest_framework import routers
from shorturls.viewset import ViewUrlViewSet,GetShortUrlViewSet,GetFriendlyNameViewSet,OriginViewSet
class ApiDocumentView(routers.APIRootView):
  """ 
                                   Getshorturl:
                Request:
                {
                    "origin_domain": "http://127.0.0.1:8000/url5/"
                }
                Response:
                {
                    "origin_domain": "http://127.0.0.1:8000/url67rrr/",
                    "short_url": "http://127.0.0.1:8000/q/Cp"
                }



                                  Friendlyname:
  Request:
                 {
                    "origin_domain": "http://127.0.0.1:8000/url/",
                    "friendly_name": "KimJardasn"
                }
  Response:
                {
                        "origin_domain": "http://127.0.0.1:8000/url5/",
                            "friendly_name": "KimKad",
                            "friendly_key": 9822967559
                        "
                 }


                                   Fullentry:
 Response:
                {
                        "id": 176,
                        "origin_domain": "http://127.0.0.1:8000/url5/",
                        "short_url": "http://127.0.0.1:8000/q/KimKad",
                        "friendly_name": "KimKad",
                        "origin_ip": "",
                        "views": 0,
                        "friendly_key": 9822967559
                    }
    """""
class DoumentedRouter(routers.DefaultRouter):
    APIRootView = ApiDocumentView

router = DoumentedRouter()

router.register(r'getshorturl',GetShortUrlViewSet,'getshorturl')
router.register(r'rdr',OriginViewSet,'Redirect')
router.register(r'friendlyname',GetFriendlyNameViewSet,basename='friendlyentry')
router.register(r'fullentry',ViewUrlViewSet,basename='fullentry')