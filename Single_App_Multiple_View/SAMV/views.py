from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def V1(request):
    return(HttpResponse('NOPE... TRY HACK ME'))

def V2(request):
    return(HttpResponse('<h1>HAHA FAILED</h1>)'))

def V3(request):
    return(HttpResponse('<script>alert("1")</script>'))