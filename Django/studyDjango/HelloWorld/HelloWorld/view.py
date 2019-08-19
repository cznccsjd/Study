#coding:utf-8

from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world!this is my first django project")

def index(requests):
    return render(requests, "index.html")