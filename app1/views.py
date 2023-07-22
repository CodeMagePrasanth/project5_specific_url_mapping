from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1>this my first project</h1>')

def second_app1(reques):
    return HttpResponse('<h3>this app1 second string</h3>')

def third_app1(reques):
    return HttpResponse('<h3>this app1 third string</h3>')