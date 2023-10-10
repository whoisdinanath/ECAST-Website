from django.urls import path, include
from .views import CommitteeMemberCreate
from .viewsets import SocialMediaViewset, CommitteeMemberViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'socials', SocialMediaViewset)
router.register(r'members', CommitteeMemberViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('member/create/', CommitteeMemberCreate.as_view()),
]
