from django.urls import path
from pk.views import *
app_name='pk'
urlpatterns=[
    path('livingstone/',livingstone,name='livingstone'),
    path('samcurran/',samcurran,name='samcurran'),

]