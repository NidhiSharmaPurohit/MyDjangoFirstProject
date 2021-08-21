from django.shortcuts import render
from cbvApp.models import Student
from cbvApp.serializer import StudentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import *


# Create your views here.

class StudentList(APIView):

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students , many=True)
        return  Response(serializer.data)

    def post(self,request):
        serializer =  StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)



class StudentDetail(APIView):
    def get_object(self,pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExits:
            raise Http404
    def get(self,request,pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self,request,pk):
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        raise Http404

    def delete(self,request,pk):
        student = self.get_object(pk)
        student.delete()




