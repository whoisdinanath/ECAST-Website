from rest_framework import serializers
from .models import CommitteeMembers, MemberTenure, MemberPosition


class CommitteeMembersSerializer(serializers.ModelSerializer):
    # position = serializers.StringRelatedField()
    position = serializers.PrimaryKeyRelatedField(
        queryset=MemberPosition.objects.all())
    # year = serializers.StringRelatedField()
    year = serializers.PrimaryKeyRelatedField(
        queryset=MemberTenure.objects.all())

    class Meta:
        model = CommitteeMembers
        # fields = ('__all__')
        fields = ['name', 'position', 'socialMedia', 'memberPhoto', 'year']


class MemberPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberPosition
        fields = ('__all__')


class MemberTenureSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberTenure
        fields = ('__all__')
