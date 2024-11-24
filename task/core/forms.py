from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario', 'label': 'Nombre de Usuario'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'label': 'Contraseña'})
    )

class SignupForm(UserCreationForm):
    class Meta:
        model= User
        fields = ["username", "email"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario', 'label': 'Nombre de Usuario'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'label': 'Ingrese Email'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'label': 'Ingrese Contraseña'}),
        }