from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def login(request):
#     return HttpResponse('first app loaded in django')
def login(request):
    return render(request,'login.html')
def home(request):
    return render(request,'home.html')
def registration(request):
    return render(request,'registration.html')
def appointment(request):
    return render(request,'appointment.html')

