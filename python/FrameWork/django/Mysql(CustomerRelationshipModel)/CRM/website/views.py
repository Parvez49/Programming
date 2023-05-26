from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
from .forms import AddRecordForm

from .forms import RegistrationForm
# Create your views here.

def home(request):
    records = Record.objects.all()
    if request.method=="POST":
        username=request.POST['user_name']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been Logged In!")
            return redirect('home')
        else:
            messages.success(request,"There was and error logging in, try again")
            return redirect('home')
    return render(request,'home.html',{'records':records})


def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request,"Logged out..")
    return redirect('home')


def register(request):
    
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfully logged in")
            return redirect('home')
    else:
        form=RegistrationForm()
        return render(request,'register.html',{'form':form})
    
    return render(request,'register.html',{'form':form})


def customer_record(request,pk):
    if request.user.is_authenticated:
        cus_rec=Record.objects.get(id=pk)
        return render(request,'record.html',{"customer_record":cus_rec})
    else:
        messages.success(request,"You must be logged in first")
        return redirect('home')
    
def delete_record(request,pk):
    if request.user.is_authenticated:
        cus_rec=Record.objects.get(id=pk)
        cus_rec.delete()
        messages.success(request,"You have successfully delete")
        return redirect('home')
    else:
        messages.success(request,"You must be logged in first")
        return redirect('home')
    
def update_record(request,pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')