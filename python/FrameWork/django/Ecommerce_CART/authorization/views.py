from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from .utils import generate_token

from django.core.mail import EmailMessage, send_mail
from django.conf import settings

from django.contrib.auth import authenticate, login, logout

from django.views.generic import View
from django.utils.encoding import force_str
# Create your views here.

def user_login(request):
    if request.method=="POST":
        username=request.POST['email']
        password=request.POST['pass1']
        user=authenticate(username=username,password=password)
        print(user)

        if user is not None:
            login(request,user)
            messages.success(request,"Login Success")
            return redirect('/')
        else:
            messages.info(request,"Verify your email")
    return render(request,"authorization/login.html")

def user_logout(request):
    return redirect("/auth/login/")

def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        con_password=request.POST['pass2']
        if password!=con_password:
            messages.warning(request,'Password is not matching')
            return render(request,'authorization/signup.html')
        try:
            if User.objects.get(username=email):
                messages.info(request,"Email is already registered!")
                return render(request,'authorization/signup.html')
        except Exception as identifier:
            pass
        user=User.objects.create_user(email,email,password)
        user.is_active=False
        user.save()

        email_subject="Activate your account"
        message=render_to_string('authorization/activate.html',{
            'user':user,
            'domain':'127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user)
        })

        #send_mail(email_subject,message,settings.EMAIL_HOST_USER,[email])
        email_message=EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
        email_message.send()
        messages.success(request,f"Activate Your Account by clicking the link in your gmail {message}")
        return redirect('/auth/login/')
    
    return render(request, "authorization/signup.html")

class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifer:
            user=None
        
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,"Account Activates Successfully")
            return redirect('/auth/login')
        return render(request,'activationfail.html')
