# you can actually name this file anythine, but by convention it is called urls.py.
# this file will map through all the urls

from django.urls import path
from . import views


# create route using the path
# ever app has their own URL configuration and needs to be included to the main application
urlpatterns = [
    path('hello/', views.say_hello),
]