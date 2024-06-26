from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import Worksheet
from . forms import WorksheetForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from requestitem.models import Message


# Create your views here.

class WorksheetAddView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    form_class = WorksheetForm
    model = Worksheet
    template_name = "worksheets/add.html"
    success_url = reverse_lazy('worksheet_list')
    login_url = 'login'
    success_message = "%(standard)s Class %(chapter)s Worksheet was added successfully" 
   

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    

class WorksheetListView(ListView):
    model = Worksheet
    context_object_name = 'worksheets'
    template_name="worksheets/list.html"
    paginate_by = 9
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = Message.objects.filter(request_for = 'worksheet')
        return context
    

class WorksheetUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Worksheet
    template_name = "worksheets/update.html"
    success_url = reverse_lazy('worksheet_list')
    form_class = WorksheetForm
    login_url='login'
    success_message = "%(standard)s Class %(chapter)s Worksheet was updated successfully" 

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class WorksheetDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = Worksheet
    template_name = "worksheets/delete.html"
    success_url = reverse_lazy('worksheet_list')
    login_url = 'login'     
    context_object_name ='worksheet'
    
    def get_success_message(self, cleaned_data):
        return f'{self.object.standard} Class {self.object.chapter} Worksheet has been deleted'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

