from rest_framework.viewsets import ModelViewSet
from .models import Project
from .serializer import ProjectSerializer


class ProjectViewset(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_context(self):
        return {'request': self.request}
