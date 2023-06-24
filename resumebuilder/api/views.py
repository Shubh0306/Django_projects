from django.shortcuts import render
from rest_framework import response
from api.models import profile
from api.serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.
class profileView(APIView):
    def post(self,request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response({'msg': 'Resume Uploaded Successfully',
                             'status':'success', 'candidate' : serializer.data})
        
        return response(serializer.errors)
    
    def get(self,request, format=None):
        candidates = profile.objects.all()
        serializer = ProfileSerializer(candidates, many=True)
        return response({'status':'success', 'candidates' : serializer.data})
        



