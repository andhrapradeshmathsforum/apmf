from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . admin import UserCreationForm

# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
