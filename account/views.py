from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'accounts/../templates/signup.html')
    elif request.method == 'POST':
        user_name = request.POST['用户名']
        password1 = request.POST['密码']
        password2 = request.POST['确认密码']
        try:
            User.objects.get(username=user_name)
            return render(request, 'accounts/../templates/signup.html', {'Username_error': 'The user already exists'})
        except User.DoesNotExist:
            if password1 == password2:
                User.objects.create_user(username=user_name, password=password1)
                return redirect('主页')
            else:
                return render(request, 'accounts/../templates/signup.html', {'Pass_Wrong': 'Inconsistent entry password'})


def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/../templates/login.html')
    elif request.method == 'POST':
        user_name = request.POST['用户名']
        pass_word = request.POST['密码']
        user = auth.authenticate(username=user_name,password=pass_word)
        if user is None:
            return render(request, 'accounts/../templates/login.html', {'Error': 'Wrong user name or password'})
        else:
            auth.login(request, user)
            return redirect('主页')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('主页')






		



	