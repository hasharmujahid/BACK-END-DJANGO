from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Single_function(request):
    return(HttpResponse('WHOAMI !!! '))
    