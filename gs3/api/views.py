from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.
# Model Object - single Student Data

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
  def get(self, request, *args, **kwargs):
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    id = pythondata.get('id',None)
    if id is not None:
      stu = Student.objects.get(id=id)
      serializer = StudentSerializer(stu)
      json_data = JsonResponse().render(serializer.data)
      return HttpResponse(json_data, content_type='application/json')
    
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
  

  def post(self, request, *args, **kwargs):
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    serializer = StudentSerializer(data = pythondata)
    if serializer.is_valid():
      serializer.save()
      res = {'msg': 'Data Created'}
      json_data = JSONRenderer().render(res)
      return HttpResponse(json_data, content_type='application/json')
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type='application/json')
    


  def put(self, request, *args, **kwargs):
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    id = pythondata.get('id')
    stu = Student.objects.get(id=id)


    serializer = StudentSerializer(stu, data=pythondata,partial=True)
    if serializer.is_valid():
      serializer.save()
      res = {'msg':'Data Updated !!'}
      json_data = JSONRenderer().render(res)
      return HttpResponse(json_data, content_type='application/json')
    

  def delete(self, request, *args, **kwargs):
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    id = pythondata.get('id')
    stu = Student.objects.get(id=id)
    stu.delete()
    res= {'msg': 'Data deletedddd!!'}
    return JsonResponse(res, safe=False)


      
    


     







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
