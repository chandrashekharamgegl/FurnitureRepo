from django.urls import path, include
from factory_app.views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('table', TableModelViewSet)
router.register('leg', LegModelViewSet)
router.register('feet', FeetModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]