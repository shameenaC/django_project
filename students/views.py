from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    students =[
       { 'name':'shami', 'depatment':'cs'}
    ]
    return HttpResponse(students)
