from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import Examplarmath
from . forms import ExamplarmathForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from requestitem.models import Message



# Create your views here.

class ExamplarmathAddView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    form_class = ExamplarmathForm
    model = Examplarmath
    template_name = "examplarmaths/add.html"
    success_url = reverse_lazy('examplarmath_list')
    login_url = 'login'
    success_message = "%(standard)s Class  %(title)s was added successfully" 
   

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    

class ExamplarmathListView(ListView):
    model = Examplarmath
    context_object_name = 'examplarmaths'
    template_name="examplarmaths/list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = Message.objects.filter(request_for = 'examplar_math')
        return context
    

class ExamplarmathUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Examplarmath
    template_name = "examplarmaths/update.html"
    success_url = reverse_lazy('examplarmath_list')
    form_class = ExamplarmathForm
    login_url='login'
    success_message = "%(standard)s Class %(title)s was updated successfully" 

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class ExamplarmathDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = Examplarmath
    template_name = "examplarmaths/delete.html"
    success_url = reverse_lazy('examplarmath_list')
    login_url = 'login'     
    context_object_name = 'examplarmath'
    def get_success_message(self, cleaned_data):
        return f'{self.object.standard} Class {self.object.title} has been deleted'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

