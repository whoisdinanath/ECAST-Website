from rest_framework.viewsets import ModelViewSet
from .models import  SocialMedia, CommitteeMember
from .serializers import  SocialMediaReadSerializer, CommitteeMemberReadSerializer, CommitteMemberWriteSerializer


class SocialMediaViewset(ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaReadSerializer
class CommitteeMemberViewset(ModelViewSet):
    queryset = CommitteeMember.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if ('create', 'update', 'partial_update', 'destroy'):
            return CommitteMemberWriteSerializer
        return CommitteeMemberReadSerializer