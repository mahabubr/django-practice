from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentSerializer

# Create your views here.


class StudentView(APIView):
    def get(self, request, id=None):
        if id is not None:
            try:
                student = Students.objects.get(id=id)
                serializer = StudentSerializer(student)
                return Response(
                    {"status": "Success", "student": serializer.data}, status=200
                )
            except Students.DoesNotExist:
                return Response(
                    {"status": "Error", "message": "Student not found"}, status=404
                )
        else:
            # Retrieve all students
            students = Students.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(
                {"status": "Success", "students": serializer.data}, status=200
            )

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def patch(self, request, id):
        result = Students.objects.get(id=id)
        serializer = StudentSerializer(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
