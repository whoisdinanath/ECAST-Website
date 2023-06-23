from rest_framework import serializers
from .models import CommitteeMembers, MemberTenure, MemberPosition



class CommitteeMembersSerializer(serializers.ModelSerializer):
    position = serializers.StringRelatedField()
    year = serializers.StringRelatedField()
    
    class Meta:
        model = CommitteeMembers
        fields = ('__all__')
    


class MemberPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberPosition
        fields = ('__all__')


class MemberTenureSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberTenure
        fields = ('__all__')


