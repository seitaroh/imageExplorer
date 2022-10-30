from rest_framework import routers
from .views import ImageViewSet, VideoViewSet, CardViewSet, MainViewSet, PageViewSet


router = routers.DefaultRouter()
router.register(r'images', ImageViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'cards', CardViewSet)
router.register(r'mains', MainViewSet)
router.register(r'pages', PageViewSet)
