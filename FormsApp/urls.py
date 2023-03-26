from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name='login'),
    path('Prof/', Prof, name='Prof'),
    path('delete/<id>', delete, name='delete'),
    path('update/<id>', update, name='update'),
    path("search/", search, name= "search"),
]
