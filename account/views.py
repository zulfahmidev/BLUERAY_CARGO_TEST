from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import EmailLoginForm, RegisterForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # redirect kalau sudah login

    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)  # username = email
            if user is not None:
                login(request, user)
                return redirect('home')  # ganti sesuai kebutuhan
            else:
                form.add_error(None, 'Email atau password salah')
    else:
        form = EmailLoginForm()

    return render(request, 'login.html', {'form': form})