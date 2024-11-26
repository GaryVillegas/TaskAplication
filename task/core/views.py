from django.shortcuts import render
from .forms import *
from .models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    taskform = TaskForm()
    if request.method == "POST":
        taskform = TaskForm(request.POST)
        if taskform.is_valid():
            taskform.save()
        else:
            # Debug: Agrega esta línea para inspeccionar errores del formulario
            print("Errores del formulario:", taskform.errors)
    return render(request, "core/index.html", {"taskform": taskform})

def task(request):
    tasks = Task.objects.all()
    return render(request, 'partials/task_table.html', {'task': tasks})

@csrf_exempt
def delete_tasks(request):
    if request.method == "POST":
        data = json.loads(request.body)
        ids = data.get("ids", [])
        Task.objects.filter(id__in=ids).delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False}, status=400)

# def loginModal(request):
#     form = LoginForm()
#     if request.method == "GET":
#         form = LoginForm()
#         return render(request, 'partials/loginModal.html', {'form': form})

#     elif request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return JsonResponse({'success': True})  # Éxito
#             else:
#                 return JsonResponse({'success': False, 'error': 'Credenciales inválidas'})  # Error
#         return JsonResponse({'success': False, 'error': 'Formulario inválido'})  # Validación fallida
#     return render(request, 'partials/loginModal.html', {'form': form})

# def signupModal(request):
#     form = SignupForm()
#     if request.method == "GET":
#         form = SignupForm()
#         return render(request, 'partials/signupModal.html', {'form': form})
#     elif request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'success': True})
#         return JsonResponse({'success': False, 'errors': form.errors})

#     return render(request, 'partials/signupModal.html', {'form': form})