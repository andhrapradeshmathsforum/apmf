from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import Ict
from . forms import IctForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from requestitem.models import Message



# Create your views here.

class IctAddView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    form_class = IctForm
    model = Ict
    template_name = "icts/add.html"
    success_url = reverse_lazy('ict_list')
    login_url = 'login'
    success_message = "%(title)s site was added successfully" 
   

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    

class IctListView(ListView):
    model = Ict
    context_object_name = 'icts'
    template_name="icts/list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = Message.objects.filter(request_for = 'ict')
        return context
    

class IctUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Ict
    template_name = "icts/update.html"
    success_url = reverse_lazy('ict_list')
    form_class = IctForm
    login_url='login'
    success_message = "%(title)s site was updated successfully" 

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class IctDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = Ict
    template_name = "icts/delete.html"
    success_url = reverse_lazy('ict_list')
    login_url = 'login'     
    context_object_name ='ict'
    def get_success_message(self, cleaned_data):
        return f'{self.object.title} site has been deleted'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


