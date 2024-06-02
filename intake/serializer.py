from .models import IntakeForm
from rest_framework import serializers

class IntakeFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntakeForm
        fields = '__all__'

    