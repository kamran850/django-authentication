from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=50,
        label='Username',
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        required=True,
    )
    email = forms.EmailField(
        required=True, 
        label='Email address',
        widget=forms.EmailInput(attrs={'placeholder': 'Email address'}),
        )
    password1 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'New password'})
        )
    password2 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'})
        )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LogInForm(AuthenticationForm):
    class Meta:
       fields = ("username", "password")
