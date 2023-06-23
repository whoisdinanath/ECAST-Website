from django.urls import path
from .views import CommitteeList, CommitteeDetail, TenureList, TenureDetail, PositionList, PositionDetail


urlpatterns = [
    path('committee/', CommitteeList.as_view()),
    path('committee/<int:pk>/', CommitteeDetail.as_view()),
    path('tenureList/', TenureList.as_view()),
    path('tenure/<int:pk>/', TenureDetail.as_view()),
    path('position/', PositionList.as_view()),
    path('position/<int:pk>/', PositionDetail.as_view()),
]


