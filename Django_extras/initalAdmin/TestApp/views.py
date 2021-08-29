from django.shortcuts import render, redirect
from .forms import RegisterForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def index(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Successfully created "+user)
            return redirect('/login')
    context = {
        'regform': form
    }
    return render(request, 'index.html', context)

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        bound_form = RegisterForm(request.POST)
        print(bound_form.is_valid())
        print(bound_form.errors)
        return redirect('/index')