from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/')

        else:
            return render(request, 'authenticate/login.html', {'error': "Invalid username or password!"})

    return render(request, 'authenticate/login.html')



def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confPass = request.POST.get('confirm_password')
        email = request.POST.get('email')

        if not username.isalnum():
            return render(request, 'authenticate/signUp.html', {'error': "Username Must Be Letters & Numbers Only!"})

        if User.objects.filter(username=username):
            return render(request, 'authenticate/signUp.html', {'error': 'User Already Exists! Try Another Username'})

        if password != confPass:
            return render(request, 'authenticate/signUp.html', {'error': "Password Didin't Match!"})
        
        if User.objects.filter(email=email):
            return render(request, 'authenticate/signUp.html', {'error': 'Email Already Exists! Try Another Email'})

        newUser = User.objects.create_user(username, email, password, is_staff = False)
        newUser.save()

        return redirect('../auth/login')


    return render(request, 'authenticate/signUp.html')

def logout(request):
    auth_logout(request)
    return redirect('../auth/login')