from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("Hello")
    return render(request,"app/index.html")
