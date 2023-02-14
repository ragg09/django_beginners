from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# takes request and return response
# basically, views in django are request handlers and not an actual html template


def say_hello(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
 