from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sumit(request):
    return HttpResponse("<h1>hello this is Sumit</h1>")