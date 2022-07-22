from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here
def books(request):
    if request.user.is_authenticated:
        return render(request, 'itemsapp/books.html')
    else:
        return redirect('/books/signin')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/books')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('/books')

        else:
            return render(request, 'itemsapp/signup.html', {'form':form})

    else:
        form = UserCreationForm()
        return render(request, 'itemsapp/signup.html', {'form':form})

def signin(request):
    if request.user.is_authenticated:
        return redirect('/books')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/books')
        else:
            form = AuthenticationForm()
            return render(request, 'itemsapp/signin.html', {'form':form})

    else:
        form = AuthenticationForm()
        return render(request, 'itemsapp/signin.html', {'form':form})

def signout(request):
    logout(request)
    return redirect('/books/signin')



