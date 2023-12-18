from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4>HELLO WORLD</h4>")

def about(request):
    return HttpResponse("<h4>HELLO WORLD 2.0</h4>")