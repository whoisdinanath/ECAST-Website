from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import CommitteeMember, MemberPosition
from .serializers import CommitteeMemberSerializer, MemberPositionSerializer

class CommitteeList(generics.ListCreateAPIView):
    serializer_class = CommitteeMemberSerializer

    def get_queryset(self):
        queryset = CommitteeMember.objects.all()
        position = self.request.query_params.get('position')
        tenure = self.request.query_params.get('year')
        if position is not None:
            queryset = queryset.filter(position=position)
        if tenure is not None:
            queryset = queryset.filter(year=tenure)
        return queryset


class CommitteeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommitteeMemberSerializer
    queryset = CommitteeMember.objects.all()




class PositionList(generics.ListCreateAPIView):
    serializer_class = MemberPositionSerializer
    queryset = MemberPosition.objects.all()


class PositionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MemberPositionSerializer
    queryset = MemberPosition.objects.all()

