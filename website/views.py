from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#AAGR KOI USER NEW H, AND HUM CHAHTE H KI VO JAB VO PAGE PR AYE TO USE LOGIN KA NOTIFICATION MILE USKE LIYE ...
def home(request):
    #Check if user is logging in
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        # AUTHENTICATE
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Are Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There is an error in logging in, Please try again!")
            return redirect('home')
    else:
        return render(request, 'home.html', {})   
    

def login_user(request):
    pass

 

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')


def register_user(request):
    return render(request, 'register.html', {})