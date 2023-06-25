from rest_framework import serializers
from .models import CommitteeMember, MemberTenure, MemberPosition


class CommitteeMemberSerializer(serializers.ModelSerializer):
    position = serializers.SlugRelatedField(queryset = MemberPosition.objects.all(), slug_field='position')
    year = serializers.SlugRelatedField(queryset = MemberTenure.objects.all(), slug_field = 'year')

    class Meta:
        model = CommitteeMember
        fields = ['name', 'position', 'facebook', 'linkedin', 'github', 'memberPhoto', 'year']



class MemberPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberPosition
        fields = ['position']



class MemberTenureSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberTenure
        fields = ['year']
