from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import Handbook
from . forms import HandbookForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

class HandbookAddView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = HandbookForm
    model = Handbook
    template_name = "handbooks/add.html"
    success_url = reverse_lazy('handbook_list')
    login_url = 'login'
    success_message = "%(standard)s Class %(title)s was added successfully" 
   

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    

class HandbookListView(ListView):
    model = Handbook
    context_object_name = 'handbooks'
    template_name="handbooks/list.html"
    

class HandbookUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Handbook
    template_name = "handbooks/update.html"
    success_url = reverse_lazy('handbook_list')
    form_class = HandbookForm
    login_url='login'
    success_message = "%(standard)s Class %(title)s was updated successfully" 

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class HandbookDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = Handbook
    template_name = "handbooks/delete.html"
    success_url = reverse_lazy('handbook_list')
    login_url = 'login'     
    context_object_name = 'handbook'
    def get_success_message(self, cleaned_data):
        return f'{self.object.standard} Class {self.object.title} has been deleted'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

