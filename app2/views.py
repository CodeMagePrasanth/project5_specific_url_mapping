from django.shortcuts import render
from django.http import HttpResponse

def first_app2(reques):
    return HttpResponse('<h3>this app2 first string</h3>')