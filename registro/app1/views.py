from django.shortcuts import render

# Create your views here.


def Home(request):
    return render(request, 'home.html')


def SignUp(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        print(uname, email, pass1, pass2)

    return render(request, 'signup.html')


def Login(request):
    return render(request, 'login.html')
