from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import Mcq
from . forms import McqForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from requestitem.models import Message



# Create your views here.

class McqAddView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    form_class = McqForm
    model = Mcq
    template_name = "mcqs/add.html"
    success_url = reverse_lazy('mcq_list')
    login_url = 'login'
    success_message = "%(standard)s Class %(chapter)s was added successfully" 
   

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    

class McqListView(ListView):
    model = Mcq
    context_object_name = 'mcqs'
    template_name="mcqs/list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = Message.objects.filter(request_for = 'mcq')
        return context
    

class McqUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Mcq
    template_name = "mcqs/update.html"
    success_url = reverse_lazy('mcq_list')
    form_class = McqForm
    login_url='login'
    success_message = "%(standard)s Class %(chapter)s was updated successfully" 

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class McqDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = Mcq
    template_name = "mcqs/delete.html"
    success_url = reverse_lazy('mcq_list')
    login_url = 'login'     
    context_object_name ='mcq'
    def get_success_message(self, cleaned_data):
        return f'{self.object.standard} Class {self.object.chapter}  has been deleted'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


