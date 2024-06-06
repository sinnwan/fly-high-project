from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import LoginUser
from django.contrib.auth import authenticate,logout,login

# Create your views here.
def home(request):
    return render(request,'home.html')


def Login(request):
    if request.method=="POST":
        username=request.POST['user_name']
        password=request.POST['password']

        data = authenticate(username=username,
                            password=password)
        if data is not None:
            login(request,data)
            if data.user_type=="user":
                return redirect(profile)
            elif data.user_type=="company":
                return HttpResponse("company model")
            else:
                return HttpResponse("no user found")

        else:
            return render(request, 'login.html',{'error':'Invalid credentials'})
    else:
        return render(request,'login.html')

def user(request):
    if request.method=='POST':
        username=request.POST['user_name']
        email=request.POST['email']
        phone_no=request.POST['phone_no']
        password=request.POST['password']

        data = LoginUser.objects.create_user(user_name=username,
                                             email=email,
                                             phone_no=phone_no,
                                             password=password,
                                             user_type="user")
        data.save()
        return HttpResponse("USER REGISTERED")
    else:
        return render(request,'register.html')


def company(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        phone=request.POST['phone']
        username=request.POST['username']
        password=request.POST['password']

        data = LoginUser.objects.create_user(first_name=first_name,
                                             phone=phone,
                                             username=username,
                                             password=password,
                                             user_type="company")
        data.save()
        return HttpResponse("COMPANY REGISTERED")
    else:
        return render(request,'register.html')


def profile(request):
    data=LoginUser.objects.get(id=request.user.id)
    return render(request,'profile.html',{'data':data})

def Logout(request):
    logout(request)
    return redirect(Login)