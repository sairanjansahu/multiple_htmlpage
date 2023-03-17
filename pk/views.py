from django.shortcuts import render

# Create your views here.

def livingstone(request):
    return render(request,'livingstone.html')

def samcurran(request):
    return render(request,'samcurran.html')