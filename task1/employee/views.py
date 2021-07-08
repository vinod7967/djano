from django.shortcuts import render
from django.http import HttpResponse
def greeting(request):
    return HttpResponse("<h1>vinod kumar</h1>")
# Create your views here.
