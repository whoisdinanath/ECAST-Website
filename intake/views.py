from django.shortcuts import render
from .models import IntakeForm
from .serializer import IntakeFormSerializer
# Create your views here.

from rest_framework import viewsets

class IntakeFormViewSet(viewsets.ModelViewSet):
    queryset = IntakeForm.objects.all()
    serializer_class = IntakeFormSerializer

