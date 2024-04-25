from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Tlm
from .forms import TlmForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from requestitem.models import Message


# Create your views here.

class TlmListView(ListView):
    model = Tlm
    template_name = "tlms/list.html"
    context_object_name = 'tlms'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = Message.objects.filter(request_for = 'tlm_photos')
        return context


class TlmAddView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Tlm
    form_class = TlmForm
    template_name = "tlms/add.html"    
    login_url = 'login'
    success_url = reverse_lazy('tlm_list')
    success_message = '%(title)s photo was uploaded successfully.'
    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    


class TlmUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Tlm
    form_class = TlmForm
    template_name = "tlms/update.html"
    login_url = 'login'
    success_url = reverse_lazy('tlm_list')
    success_message = '%(title)s photo was updated successfully.'
    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)
    
    
    


class TlmDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = Tlm
    template_name = "tlms/delete.html"
    context_object_name = 'tlm'
    login_url = 'login'
    success_url = reverse_lazy('tlm_list')

    def get_success_message(self, cleaned_data: dict[str, str]) -> str:        
        return f"{self.object.title} photo was deleted successfully"
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
    
class TlmDetailView(DetailView):
    model = Tlm
    template_name='tlms/details.html'
    context_object_name = 'tlm'



