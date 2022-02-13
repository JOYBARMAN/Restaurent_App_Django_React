from rest_framework import routers
from .viewsets import MenuViewset


router=routers.DefaultRouter()
router.register(r'menu',MenuViewset,basename='menu')
