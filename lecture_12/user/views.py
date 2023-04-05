from django.shortcuts import render, redirect
from user.forms import UserRegistrationForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import login, logout


def login_page(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.data.get('username'), password=form.data.get('password'))
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'user/login.html', {'form': form})
        else:
            return render(request, 'user/login.html', {'form': form})


def logout_page(request):
    logout(request)
    return redirect('/auth/login')


def register_page(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
        return render(request, 'user/register.html', {'form': form})
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('/auth/login/')
        else:
            return render(request, 'user/register.html', {'form': form})

