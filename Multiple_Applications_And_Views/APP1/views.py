import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def V1(request):
    return (HttpResponse("RESPONSE FROM APP1 AND V1"))
def V2(request):
    return (HttpResponse("RESPONSE FROM APP1 AND V2"))
