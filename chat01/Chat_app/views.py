from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    # return HttpResponse("template")
    return render(request, "chat/home.html", {})  # response

def login(request):
    return render(request, "chat/login.html", {})