from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1>this my first project</h1>')