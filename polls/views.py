from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Suman. You are at the polls index.")
