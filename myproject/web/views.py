from django.shortcuts import render
from django.http import HttpResponse
def Nhap(request): 
    return render(request,'home.html')
def LOG(request): 
    return render(request,'login.html')
def REG(request): 
    return render(request,'register.html')

