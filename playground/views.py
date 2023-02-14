from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# takes request and return response
# basically, views in django are request handlers and not an actual html template

# actual views in django is called template, it holds the html elements


def say_hello(request):
    return render(request, 'hello.html', {'name': 'RENE' })

 