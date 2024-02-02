from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm 
from .models import Record


#AAGR KOI USER NEW H, AND HUM CHAHTE H KI VO JAB VO PAGE PR AYE TO USE LOGIN KA NOTIFICATION MILE USKE LIYE ...
def home(request):
    records = Record.objects.all()
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
        return render(request, 'home.html', {'records':records})   
    

 

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #AUTHENTICATE AND LOGIN
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password = password)
            login(request, user)
            messages.success(request, "YOU HAVE SUCCESSFULLY REGISTERED.")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
        
    return render(request, 'register.html', {'form': form})



def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "YOU MUST BE LOGGED IN TO VIEW THAT PAGE.")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted")
        return redirect('home')
    else:
        messages.success(request, "YOU MUST BE LOGGED IN TO VIEW THAT PAGE.")
        return redirect('home')
 
   
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method =="POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "RECORD ADDED")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "YOU MUST LOG IN!")
        return redirect('home')
    
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance = current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been Updated!")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "YOU MUST LOG IN!")
        return redirect('home')
