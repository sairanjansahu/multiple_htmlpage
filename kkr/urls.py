from django.urls import path
from kkr.views import *
app_name='kkr'
urlpatterns=[
    path('russell/',russell,name='russell'),
    path('iyer/',iyer,name='iyer'),
]