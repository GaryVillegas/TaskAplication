from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('loginModal', loginModal, name='loginModal'),
    path('signupModal', signupModal, name='signupModal')
]