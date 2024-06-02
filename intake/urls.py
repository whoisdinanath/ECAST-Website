from django.urls import path, include
from .views import IntakeListCreate, IntakeDetail

urlpatterns = [
    path('form/', IntakeListCreate.as_view(), name='intake-list-create'),
    path('form/<int:pk>/', IntakeDetail.as_view(), name='intake-detail'),
]