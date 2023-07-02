from django.urls import path, include
from .views import CommitteeList, CommitteeDetail
from .viewsets import PositionViewset, SocialMediaViewset, CommitteeMemberViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'positions', PositionViewset)
router.register(r'socials', SocialMediaViewset)
router.register(r'members', CommitteeMemberViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('committee/', CommitteeList.as_view()),
    path('committee/<int:pk>/', CommitteeDetail.as_view()),
]


