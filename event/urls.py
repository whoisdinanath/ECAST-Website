from rest_framework.routers import DefaultRouter
from .viewsets import EventViewset, NewsletterViewset, ImageViewset
from django.urls import path, include
from .views import EventCreateView, NewsletterCreateView, ImageCreateView

router = DefaultRouter()
router.register('events', EventViewset, basename='event')
router.register('newsletter', NewsletterViewset, basename='newsletter')
router.register('images', ImageViewset, basename='image')

urlpatterns = [
    path('', include(router.urls)),
    path('event/create/', EventCreateView.as_view()),
    path('newsletter/create/', NewsletterCreateView.as_view()),
    path('image/create/', ImageCreateView.as_view()),

]
