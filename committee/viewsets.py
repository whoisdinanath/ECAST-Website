from rest_framework.viewsets import ModelViewSet
from .models import MemberPosition, SocialMedia, CommitteeMember
from .serializers import MemberPositionSerializer, SocialMediaSerializer, CommitteeMemberSerializer

class PositionViewset(ModelViewSet):
    queryset = MemberPosition.objects.all()
    serializer_class = MemberPositionSerializer

class SocialMediaViewset(ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

class CommitteeMemberViewset(ModelViewSet):
    queryset = CommitteeMember.objects.all()
    serializer_class = CommitteeMemberSerializer