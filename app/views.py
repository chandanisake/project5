from django.shortcuts import render

#create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('this is my first fbv')
def second(request):
    return HttpResponse('this is my second fbv')
def home(request):
    return render(request,'home.html')
def home1(request):
    return render(request,'home1.html')

