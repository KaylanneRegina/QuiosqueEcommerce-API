from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.shortcuts import redirect, render
from django.urls import reverse


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username = username, password = password)

        if not user:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha invalidos')
            return redirect(reverse('login'))

        auth.login(request, user)
        return redirect('produtos')    

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        user = User.objects.filter(username = username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'O email ja existe!')
            return redirect(reverse('cadastro'))

        user = User.objects.create_user(
            username = username,
            email = email,
            password = password,
        ) 
        return redirect(reverse('login')) 


def contato(request):
    return render(request, 'contato.html')