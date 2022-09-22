from django.contrib.auth.hashers import check_password
from .models import *
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from .forms import SignUpForm

# Create your views here.
def index(request):
    category1 = Category.objects.all()
    categoryID = request.GET.get("category")
    if categoryID:
        product1 = Product.objects.filter(sub_category = categoryID)
    else:
        product1 = Product.objects.all()
    context = {
        "category2":category1,
        "product2":product1
    }
    print(request.session.get("user_username"))
    return render(request,"store/index.html",context)


#signup
def signup(request):
    if request.method =="POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = SignUpForm()
    return render(request,"store/signup.html",{"form":fm})

#Login
def signin(request):
    if request.method =="POST":
        fm = AuthenticationForm(request = request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data["username"]
            upass = fm.cleaned_data["password"]
            userO = authenticate(username = uname,password = upass)
            if userO is not None:
                request.session["user_username"] = userO.uname
                request.sessino["user_email"] = userO.email
                login(request,userO)
                return redirect("/")
    else:
        fm =AuthenticationForm()
    return render(request,"store/login.html",{"form":fm})

def logout(request):
    auth.logout(request)
    return redirect("/")

