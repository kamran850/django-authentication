from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .forms import *
from django.views.generic import TemplateView, CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


# # Create your views here
class HomeView(TemplateView):
    template_name = "home.html"


def books(request):
    if request.user.is_authenticated:
        return render(request, 'itemsapp/books.html')
    else:
        return redirect('/books/signin')

def UserRegister(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User successfully signup.')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('profile')

        else:
            messages.warning(request, 'Invalid username or password.')
            return render(request, 'auth/signup.html', {'form':form})

    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form':form})

@login_required
def UserProfile(request):
    return render(request, 'auth/profile.html')

def UserLogin(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'User successfully signin.')
            return redirect('profile')
        else:
            messages.warning(request, 'Invalid username or password.')
            return render(request, 'auth/signin.html', {'form':form})

    else:
        form = AuthenticationForm()
    return render(request, 'auth/signin.html', {'form':form})

@login_required
def UserLogout(request):
    logout(request)
    messages.info(request, 'User successfully logout.')
    return redirect('home')


def UserChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('signin')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'auth/change_password.html', {'form': form})