from rest_framework.viewsets import ModelViewSet
from .models import  SocialMedia, CommitteeMember
from .serializers import  SocialMediaReadSerializer, CommitteeMemberReadSerializer, CommitteMemberWriteSerializer


class SocialMediaViewset(ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaReadSerializer

# This viewset will handle all http request so no need to create separate views for each request
# Search views should be created separately as they are not handled by viewsets
class CommitteeMemberViewset(ModelViewSet):
    queryset = CommitteeMember.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if ('create', 'update', 'partial_update', 'destroy'):
            return CommitteMemberWriteSerializer
        return CommitteeMemberReadSerializer