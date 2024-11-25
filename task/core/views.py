from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .forms import *

# Create your views here.
def index(request):
    usuario = User.objects.all()
    context = {
        'usuario': usuario
    }
    return render(request, 'core/index.html', context)

def loginModal(request):
    form = LoginForm()
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'partials/loginModal.html', {'form': form})

    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'success': True})  # Éxito
            else:
                return JsonResponse({'success': False, 'error': 'Credenciales inválidas'})  # Error
        return JsonResponse({'success': False, 'error': 'Formulario inválido'})  # Validación fallida
    return render(request, 'partials/loginModal.html', {'form': form})

def signupModal(request):
    form = SignupForm()
    if request.method == "GET":
        form = SignupForm()
        return render(request, 'partials/signupModal.html', {'form': form})
    elif request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})

    return render(request, 'partials/signupModal.html', {'form': form})