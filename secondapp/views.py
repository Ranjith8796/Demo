from django.shortcuts import render
from django.http import HttpResponse
import datetime

def tellmetime(request):
    time=datetime.datetime.now()
    return render(request,'secondapp/telltime.html',{'result':time})

    