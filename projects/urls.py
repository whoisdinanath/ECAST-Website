from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ProjectViewset
from .views import ProjectCreateView, ProjectListView

router = DefaultRouter()
router.register(r'projects', ProjectViewset)
urlpatterns = [
    path('', include(router.urls)),
    path('create/', ProjectCreateView.as_view()),
    path('list/', ProjectListView.as_view()),
]
