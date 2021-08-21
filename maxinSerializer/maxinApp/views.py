from django.shortcuts import render
from maxinApp.models import Student
from maxinApp.serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics, mixins
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class StudentList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def get(self, request):
        return self.list(request)

    def post(self,request):
        return self.create(request)
