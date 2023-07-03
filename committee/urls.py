from django.urls import path, include
from .views import  CommitteeMemberCreate
from .viewsets import SocialMediaViewset, CommitteeMemberViewset
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'socials', SocialMediaViewset)
router.register(r'members', CommitteeMemberViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('member/create/', CommitteeMemberCreate.as_view()),
]
