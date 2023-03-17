from django.shortcuts import render

# Create your views here.

def russell(request):
    return render(request,'russell.html')

def iyer(request):
    return render(request,'iyer.html')