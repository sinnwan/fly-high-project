from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import LoginUser,user,company
from django.contrib.auth import authenticate,logout,login

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def Login(request):
    if request.method=="POST":
        user_name=request.POST['user_name']
        password=request.POST['password']
        admin_user=authenticate(request,username=user_name,password=password)
        if admin_user is not None and admin_user.is_staff:
           login(request,admin_user)
           return redirect(profile)

        data = authenticate(username=user_name,
                            password=password)
        if data is not None:
            login(request,data)
            if data.usertype=="user":
                return redirect(profile)
            elif data.usertype=="company":
                return redirect(profile)
            else:
                return render(request,'login.html',{'message':"please wait"})

        else:
            return render(request, 'login.html',{'message':'invalid credential'})
    else:
        return render(request,'login.html')

def user_register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        user_name=request.POST['user_name']
        email=request.POST['email']
        phone_no=request.POST['phone_no']
        password=request.POST['password']
        if LoginUser.objects.filter(username=user_name,usertype='user').exists():
            return render(request,'user/register.html',{'message':'username already exists'})
        if password != password:
            return render(request,'user/register.html',{'message':'invalid password'})
        try:
            login_data=LoginUser.objects.create_user(username=user_name,password=password,usertype='user')

            user_data=user.objects.create(login_id=login_data,first_name=first_name,last_name=last_name,user_name=user_name,email=email,phone_no=phone_no,password=password)
            return redirect(login)
        except Exception:
            return render(request,'user/register.html',{'message':'Error occurred'})

    else:
        return render(request,'user/register.html')


def company_register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        company_name = request.POST['company_name']
        email=request.POST['email']
        phone_no=request.POST['phone_no']
        password=request.POST['password']
        if LoginUser.objects.filter(username=company_name, usertype='company').exists():
            return render(request, 'company/register.html', {'message': 'username already exists'})
        if password != password:
            return render(request, 'company/register.html', {'message': 'invalid password'})
        login_data=LoginUser.objects.create_user(username=company_name,password=password,usertype='company')
        login_data.save()
        log_id=LoginUser.objects.get(id=login_data.id)
        company_data=company.objects.create(login_id=log_id,company_name=company_name,email=email,phone_no=phone_no,password=password)
        company_data.save()
        return redirect(Login)

    else:
        return render(request,'company/register.html')


def profile(request):
    data=LoginUser.objects.get(id=request.user.id)
    return render(request,'profile.html',{'data':data})

def edit_profile(request):
    data=LoginUser.objects.get(id=request.user.id)
    if request.method == "POST":
        data.first_name = request.POST['first_name']
        data.last_name = request.POST['last_name']
        data.user_name = request.POST['user_name']
        data.email = request.POST['email']
        data.phone_no = request.POST['phone_no']
        data.password = request.POST['password']
        data.save()
        return redirect(profile)
    else:
        return render(request,'edit-profile.html',{'data':data})

def Logout(request):
    logout(request)
    return redirect(Login)