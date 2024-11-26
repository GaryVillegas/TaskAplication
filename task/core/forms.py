from django import forms
from .models import *
from bootstrap_datepicker.widgets import DatePicker

#$class LoginForm(AuthenticationForm):
#$    username = forms.CharField(widget=forms.TextInput(attrs={#$
#$        'class': 'form-control', 'placeholder': 'Usuario', 'label': 'Nombre de usuario'}))
#$    password = forms.CharField(widget=forms.PasswordInput(attrs={
#$        'class': 'form-control', 'placeholder': 'Contraseña', 'label': 'Contraseña'}))

#class SignupForm(UserCreationForm):
#    class Meta:
#        model= User
#        fields = ["username", "email",]
#        widgets = {
#            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario', 'label': 'Nombre de Usuario'}),
#            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'label': 'Ingrese Email'}),
#        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "time_task", "description"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'label': 'Tittle'}),
            'time_task': forms.DateInput(attrs={'class': 'form-control', 'type': 'date','label': 'Time task'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'label': 'description'})
        }