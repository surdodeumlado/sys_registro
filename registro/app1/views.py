from django.shortcuts import render

# Create your views here.


def Home(request):
    pass


def SignUp(request):
    return render(request, 'signup.html')


def Login(request):
    pass
