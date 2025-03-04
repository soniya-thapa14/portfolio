from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def home(request):
    if request.method == "POST":
       cont = contact(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('message')
        )
       cont.save()
       return render(request,'base/home.html')
    return render(request,'base/home.html')
