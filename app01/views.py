from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import *
from django.views.generic import TemplateView, CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# # Create your views here
class HomeView(TemplateView):
    template_name = "home.html"


def books(request):
    if request.user.is_authenticated:
        return render(request, 'itemsapp/books.html')
    else:
        return redirect('/books/signin')

def signup(request):
    form = UserCreationForm()
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
        return render(request, 'auth/signup.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'auth/profile.html')

def signin(request):
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
            form = AuthenticationForm()
            return render(request, 'auth/signin.html', {'form':form})

    else:
        form = AuthenticationForm()
        return render(request, 'auth/signin.html', {'form':form})

@login_required
def signout(request):
    logout(request)
    messages.info(request, 'User successfully logout.')
    return redirect('home')

# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
 
# def login(request):
#     return render(request, 'login.html')
 
# @login_required
# def home(request):
#     return render(request, 'home.html')

# class SignUp(CreateView):
#     form_class = SignUpForm
#     template_name = 'auth/user_form.html'
#     success_url = '/login/'