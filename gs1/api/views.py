from django.shortcuts import render
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.
# Model Object - single Student Data

def student_detail(request, pk):
  #  first we create complex model object
  stu = Student.objects.get(id = pk)
  #  then we convert it into python object
  serializer = StudentSerializer(stu)  
  #  Then convert json data 
  json_data = JSONRenderer().render(serializer.data)
  #  then we sent to the client
  return HttpResponse(json_data, content_type='application./json')

  #  JsonResponse(serializer.data , safe=False)




 #  Query set - All student data
def student_list(request):
  #   first we create complex model object
  stu = Student.objects.all()

  #   then we convert it into python object
  serializer = StudentSerializer(stu, many=True)  
  #   Then convert json data 
  
  json_data = JSONRenderer().render(serializer.data)
  #   then we sent to the client
  return HttpResponse(json_data, content_type='application./json') 
  # JsonResponse(serializer.data, safe=False)
