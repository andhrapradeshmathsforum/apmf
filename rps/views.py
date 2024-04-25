from django.shortcuts import render
from django.urls import reverse_lazy
from . models import Rp
from . forms import RpForm
from django.views.generic import CreateView

# Create your views here.


class RpAddView(CreateView):
    model = Rp
    form_class = RpForm
    template_name = "rps/add.html"
    success_url = reverse_lazy('home')
    succcess_message = 'Your details are submitted successfully.'

