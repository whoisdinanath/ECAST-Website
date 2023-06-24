from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import CommitteeMembers, MemberPosition, MemberTenure
from .serializers import CommitteeMembersSerializer, MemberPositionSerializer, MemberTenureSerializer


class CommitteeList(generics.ListCreateAPIView):
    serializer_class = CommitteeMembersSerializer

    def get_queryset(self):
        queryset = CommitteeMembers.objects.all()
        position = self.request.query_params.get('position')
        tenure = self.request.query_params.get('year')
        if position is not None:
            queryset = queryset.filter(position=position)
        if tenure is not None:
            queryset = queryset.filter(year=tenure)
        return queryset

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CommitteeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommitteeMembersSerializer
    queryset = CommitteeMembers.objects.all()


class TenureList(generics.ListCreateAPIView):
    serializer_class = MemberTenureSerializer
    queryset = MemberTenure.objects.all()


class TenureDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MemberTenureSerializer
    queryset = MemberTenure.objects.all()


class PositionList(generics.ListCreateAPIView):
    serializer_class = MemberPositionSerializer
    queryset = MemberPosition.objects.all()


class PositionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MemberPositionSerializer
    queryset = MemberPosition.objects.all()
