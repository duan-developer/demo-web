from django.shortcuts import render
from django.http import HttpResponse
def Nhap(request): 
    return render(request,'home.html')

