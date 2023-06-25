from django.urls import path
from .views import CommitteeList, CommitteeDetail


urlpatterns = [
    path('committee/', CommitteeList.as_view()),
    path('committee/<int:pk>/', CommitteeDetail.as_view()),
]


