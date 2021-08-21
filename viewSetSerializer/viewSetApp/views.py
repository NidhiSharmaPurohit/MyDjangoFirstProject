from django.shortcuts import render
from viewSetApp.models import Student
from viewSetApp.serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #filter_backends = [DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'id']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
