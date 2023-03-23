from a_s.views import AsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('autosys', AsViewSet)
