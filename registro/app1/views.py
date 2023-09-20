from django.shortcuts import render

# Create your views here.


def Home(request):
    return render(request, 'home.html')


def SignUp(request):
    return render(request, 'signup.html')


def Login(request):
    return render(request, 'login.html')
