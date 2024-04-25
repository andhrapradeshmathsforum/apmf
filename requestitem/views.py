from django.shortcuts import render
from django.views.generic import CreateView, DeleteView
from .models import Message
from .forms import MessageForm
from django.urls import reverse_lazy

# Create your views here.

class MessageAddView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'requestitem/add.html'
    success_message = 'Your request was successfully posted.'
    success_url = reverse_lazy('home')
    