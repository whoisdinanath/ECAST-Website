from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import CommitteeMember
from .serializers import CommitteeMemberReadSerializer, CommitteMemberWriteSerializer

class CommitteeMemberCreate(generics.CreateAPIView):
    serializer_class = CommitteeMemberReadSerializer

    def post(self, request, *args, **kwargs):
        serializer = CommitteMemberWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


## search view for committee members
class CommitteeMemberSearch(generics.ListAPIView):
    serializer_class = CommitteeMemberReadSerializer

    def get_queryset(self):
        queryset = CommitteeMember.objects.all()
        name = self.request.query_params.get('name', None)
        position = self.request.query_params.get('position', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        if position is not None:
            queryset = queryset.filter(position__icontains=position)
        return queryset