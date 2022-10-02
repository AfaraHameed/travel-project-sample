from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=='POST':
        user_name = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password1']
        cpassword = request.POST['password2']
        first_name = request.POST['username']
        if password==cpassword:
            if User.objects.filter(username=user_name).exists():
                print("username already exists")
                messages.info(request,"user name already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print("email already exist")
                messages.info(request,"email already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                print("user created")
        else:
            print("password not matched")
            return  redirect('register')
        return redirect('/')
    else:
        return render(request,'registration.html')
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid details")
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')