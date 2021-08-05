from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . import models


def sahifa(request):
    mevalar = models.Meva.objects.all()
    return render(request, 'index.html', {'mevalar': mevalar})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pasword1 = request.POST['password1']
        pasword2 = request.POST['password2']

        if pasword2 == pasword1:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Bu Email band!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Bu Username band!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=pasword1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Parolni tog\'ri takrorlang!')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Login yoki parol xato!')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')



def praktika(request):
    email = request.POST['email']
    password = request.POST['password']
    return render(request, 'praktika.html', {'email': email, 'password': password})