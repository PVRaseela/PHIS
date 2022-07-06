from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from . models import *
from administration.models import *
# from administration import models as admin_models
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# def login(request):
#     return HttpResponse('first app loaded in django')
@csrf_exempt
def login(request):
    if request.method== 'POST':
        try:
        
            username=request.POST['username']
            password=request.POST['password']
            user=User.objects.get(username=username,password=password)
            print(user)
            request.session['user_id']=user.id
            return redirect('home')
        except User.DoesNotExist:
            return render(request,'login.html',{'message':'incorrect credentials entered'})
            
            
    return render(request,'login.html')

# def login(request):
#     if request.method== 'POST':
#         try:
        
#             username=request.POST['username']
#             password=request.POST['password']
#             user=User.objects.get(username=username)
#             print(user)
#             if (user.username==username) and (user.password==password):
#                 employee=Employee.objects.get(id=user.employee.id)
#                 full_name=employee.firstname+" "+employee.middlename+" "+employee.lastname
#                 print(full_name)
#                 return render(request,'home.html',{'name':full_name,} )
                
#             else:
#                  return render(request,'login.html',{'message':'incorrect credentials entered'})
            
#         except User.DoesNotExist:
#             return render(request,'login.html',{'message':'incorrect credentials entered'})

#     return render(request,'login.html')
    


@csrf_exempt
def home(request):
    var3=request.session['user_id']
    user1=User.objects.get(id=var3)
    # employee=Employee.objects.get(id=user1.employee.id)
    # print(employee)
    full_name=user1.employee.firstname+" "+user1.employee.middlename+" "+user1.employee.lastname
    return render(request,'home.html' ,{'name':full_name})
    
@csrf_exempt
def logout(request):
    return redirect("login")
    return render(request,'login.html')


def registration(request):
    return render(request,'registration.html')
def appointment(request):
    return render(request,'appointment.html')

