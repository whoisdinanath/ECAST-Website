from rest_framework import serializers
from .models import CommitteeMember,SocialMedia, MemberPosition
import uuid


class MemberPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberPosition
        fields = ['position', ]


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ('platform', 'handle')

class CommitteeMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommitteeMember
        fields = ('name', 'position', 'started_from', 'tenure', 'memberPhoto', )

