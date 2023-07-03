from rest_framework import serializers
from .models import CommitteeMember,SocialMedia
import uuid




class SocialMediaReadSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(source='user.name', read_only=True)
    class Meta:
        model = SocialMedia
        fields = ('platform', 'handle')


class CommitteeMemberReadSerializer(serializers.ModelSerializer):
    # position = serializers.CharField(source='position.position', read_only=True)
    social_media = SocialMediaReadSerializer(many=True, read_only=True)
    class Meta:
        model = CommitteeMember
        depth = 1
        fields = ('id', 'name', 'position','started_from', 'tenure', 'memberPhoto',  'social_media')
        

class CommitteMemberWriteSerializer(serializers.ModelSerializer):
    # position = MemberPositionReadSerializer()
    social_media = SocialMediaReadSerializer(many=True)

    class Meta:
        model = CommitteeMember
        fields = ('name', 'position', 'started_from', 'tenure', 'memberPhoto', 'social_media')

    def create(self, validated_data):
        print(validated_data)
        # position = validated_data.pop('position')
        # print(position)
        social_media = validated_data.pop('social_media')
        # position, created = MemberPosition.objects.get_or_create(**position)
        
        committee_member = CommitteeMember.objects.create(**validated_data)
        for social in social_media:
            SocialMedia.objects.create(user=committee_member, **social)
        return committee_member
    
    def update(self, instance, validated_data):
        # position = validated_data.pop('position')
        social_media = validated_data.pop('social_media')
        # position, created = MemberPosition.objects.get_or_create(**position)
        # instance.position = position
        instance.name = validated_data.get('name', instance.name)
        instance.started_from = validated_data.get('started_from', instance.started_from)
        instance.tenure = validated_data.get('tenure', instance.tenure)
        instance.memberPhoto = validated_data.get('memberPhoto', instance.memberPhoto)
        instance.save()
        for social in social_media:
            SocialMedia.objects.create(user=instance, **social)
        return instance