from rest_framework.routers import DefaultRouter
from .viewsets import EventViewset, NewsletterViewset
from django.urls import path, include

router = DefaultRouter()
router.register('event', EventViewset, basename='event')
router.register('newsletter', NewsletterViewset, basename='newsletter')

urlpatterns = [
    path('', include(router.urls)),

]
