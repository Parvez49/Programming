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
    logout(request)
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



from django.contrib.auth.tokens import PasswordResetTokenGenerator

class RequestResetEmailView(View):
    def get(self,request):
        return render(request,'authorization/request-reset-email.html')
    
    def post(self,request):
        email=request.POST['email']
        user=User.objects.filter(email=email)

        if user.exists():
            # current_site=get_current_site(request)
            email_subject='[Reset Your Password]'
            message=render_to_string('authorization/reset-user-password.html',{
                'domain':'127.0.0.1:8000',
                'uid':urlsafe_base64_encode(force_bytes(user[0].pk)),
                'token':PasswordResetTokenGenerator().make_token(user[0])
            })

            # email_message=EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
            # email_message.send()

            messages.info(request,f"WE HAVE SENT YOU AN EMAIL WITH INSTRUCTIONS ON HOW TO RESET THE PASSWORD {message} " )
            return render(request,'authorization/request-reset-email.html')
        
# force_text change to force_str 
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError

class SetNewPasswordView(View):
    def get(self,request,uidb64,token):
        context = {
            'uidb64':uidb64, 
            'token':token
        }
        try:
            user_id=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=user_id)

            if  not PasswordResetTokenGenerator().check_token(user,token):
                messages.warning(request,"Password Reset Link is Invalid")
                return render(request,'authorization/request-reset-email.html')

        except DjangoUnicodeDecodeError as identifier:
            pass

        return render(request,'authorization/set-new-password.html',context)
    def post(self,request,uidb64,token):
        context={
            'uidb64':uidb64,
            'token':token
        }
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,'authorization/set-new-password.html',context)
        
        try:
            user_id=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=user_id)
            user.set_password(password)
            user.save()
            messages.success(request,"Password Reset Success Please Login with NewPassword")
            return redirect('/auth/login/')

        except DjangoUnicodeDecodeError as identifier:
            messages.error(request,"Something Went Wrong")
            return render(request,'authorization/set-new-password.html',context)

        return render(request,'set-new-password.html',context)



    