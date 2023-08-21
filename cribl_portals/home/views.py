from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    return render(request, 'home.html', {})

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        # Check to see if logging in
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been logged in")
                return redirect('home')
            else:
                messages.success(request, "There was an error logging in, please try again....")
                return render(request, 'login.html', {})
        else:
            return render(request, 'login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully registered. Welcome!")
                return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {"form": form})
    
    return render(request, 'register.html', {"form": form})