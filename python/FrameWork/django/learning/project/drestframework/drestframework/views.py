from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from restdata.serializer import StudentSerializer
from restdata.models import Student

class TestView(APIView):

    def get(self,request,*args,**kwargs):
        query=Student.objects.all()
        dt=query.first()
        serializer=StudentSerializer(dt)
        #serializer=StudentSerializer(query,many=True)
        return Response(serializer.data)
    """
    def get(self,request,*args,**kwargs):
        data={
            'username':'admin',
            'years_active': 10
        }
        return Response(data)
    """

    def post(self,request,*args,**kwargs):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
