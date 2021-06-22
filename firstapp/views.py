from django.http.response import HttpResponse, HttpResponseRedirectBase
from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def welc(request):
    return render(request,'firstapp/welcome.html')
def home(request):
    return render(request,'firstapp/home.html') 
def gm_(request):
    return render(request,'firstapp/gm.html')
def ga_(request):
    return render(request,'firstapp/ga.html')
def gn_(request):
    return render(request,'firstapp/gn.html')