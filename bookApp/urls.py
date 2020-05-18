from django.urls import path, include
from .views import feedView
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('',feedView,)

urlpatterns = router.urls


