from typing import Any
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.http import HttpResponse
from .models import Course
from .serializers import CourseSerializaer
from rest_framework.response import Response
from .services import QdrantTest
from qdrant_client.http.models import PointStruct
# Create your views here.

class CoursesViewSet(viewsets.ViewSet):
    def __init__(self):
        self.qdrantTest = QdrantTest()
    def list(self, request): 
        courses = Course.objects.all()
        serializers = CourseSerializaer(courses, many = True)
        return Response(serializers.data, status= status.HTTP_200_OK)
    def create(self, resquest): 
        response = {"status": True, "message": "success"}
        sta = self.qdrantTest.create_collection('test_collection') 
        response["status"] = sta
        return Response(response, status=status.HTTP_201_CREATED)
    def addVector(self, request): 
        points_struct = []
        collection_name = request.data["collection_name"]
        points = request.data["points"]
        for point in points:
            points_struct.append(PointStruct(id=point['id'], vector=point["vector"], payload=point["payload"]))
        self.qdrantTest.add_vector(collection_name=collection_name, points=points_struct)         
        response = {"status": True, "message": "success"}
        return Response(response, status=status.HTTP_201_CREATED)