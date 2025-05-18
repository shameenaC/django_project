from django.shortcuts import render,get_object_or_404
#from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from employees.models import Employee
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins,generics,viewsets
from blogs.models import Blog,Comment
from blogs.serializers import BlogSerializer,CommentSerializer
from .paginations import CustomPagination
from employees.filters import Employeefilter
from rest_framework.filters import SearchFilter,OrderingFilter

# Create your views here.
@api_view(['GET','POST',])
def studentsview(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
       serializer = StudentSerializer(data = request.data)
       if serializer.is_valid():
           serializer.save() 
           return Response(serializer.data, status = status.HTTP_201_CREATED)
       print(serializer.errors)
       return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])  
def studentdetialview(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status =status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method =='PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
           serializer.save() 
           return Response(serializer.data, status=status.HTTP_200_OK)
        else:
          return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#class Employeeview(APIView):
    #def get(self,request):
        #employees = Employee.objects.all()
        #serializer = EmployeeSerializer(employees, many=True)
        #return Response(serializer.data, status=status.HTTP_200_OK)
    #def post(self,request):
        #serializer =EmployeeSerializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #print(serializer.errors)
        #return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

#class EmployeeDetialview(APIView):
    #def get_object(self,pk):
        #try:
            #return Employee.objects.get(pk=pk)
        #except Employee.DoesNotExist:
            #raise Http404
    
    #def get(self,request,pk):
        #employee = self.get_object(pk)
        #serializer = EmployeeSerializer(employee)
        #return Response(serializer.data, status=status.HTTP_200_OK)

    #def put(self,request,pk):
        #employee = self.get_object(pk)
        #serializer = EmployeeSerializer(employee,data=request.data)
       # if serializer.is_valid():
           #serializer.save() 
           #return Response(serializer.data, status=status.HTTP_200_OK)
        #return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
   # def deletet(self,request,pk):
        #employee = self.get_object(pk)
        #employee.delete()
        #return Response(status=status.HTTP_204_NO_CONTENT)'''

        
"""class Employeeview(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class EmployeeDetialview(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)
        """
"""class Employeeview(generics.ListCreateAPIView):
     queryset = Employee.objects.all()
     serializer_class = EmployeeSerializer 

class EmployeeDetialview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field ='pk'

"""


"""class EmployeeViewset(viewsets.ViewSet):
    def list(self,request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)
    def create(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    def retrieve(self,request,pk=None):
        employee = get_object_or_404(Employee,pk=pk)
        serializer =EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def update(self,request,pk=None):
        employee = get_object_or_404(Employee,pk=pk)
        serializer = EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self,request,pk=None):
        employee = get_object_or_404(Employee,pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination
    filterset_class = Employeefilter



class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['blog_title','blog_body']
    ordering_fields =['id','blog_title']

class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class BlogDetialView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field='pk'

class CommentDetialView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field='pk'

