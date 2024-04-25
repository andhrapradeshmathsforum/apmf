from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import Ppt
from . forms import PptForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from requestitem.models import Message



# Create your views here.

class PptAddView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    form_class = PptForm
    model = Ppt
    template_name = "ppts/add.html"
    success_url = reverse_lazy('ppt_list')
    login_url = 'login'
    success_message = "%(standard)s Class %(chapter)s PPT was added successfully" 
   

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    

class PptListView(ListView):
    model = Ppt
    context_object_name = 'ppts'
    template_name="ppts/list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = Message.objects.filter(request_for = 'ppt')
        return context
    

class PptUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Ppt
    template_name = "ppts/update.html"
    success_url = reverse_lazy('ppt_list')
    form_class = PptForm
    login_url='login'
    success_message = "%(standard)s Class %(chapter)s PPT was updated successfully" 

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class PptDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = Ppt
    template_name = "ppts/delete.html"
    success_url = reverse_lazy('ppt_list')
    login_url = 'login'     
    context_object_name ='ppt'
    def get_success_message(self, cleaned_data):
        return f'{self.object.standard} Class {self.object.chapter} PPT has been deleted'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

class PptSearchResultListView(ListView):
    model = Ppt
    context_object_name = 'ppts'
    template_name="ppts/ppt_search_result_list.html"
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Ppt.objects.filter(
            Q(standard__icontains=query) | Q(chapter__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
    
class MyPptListView(LoginRequiredMixin,ListView):
    model = Ppt
    context_object_name = 'ppts'
    template_name = 'ppts/my_ppt_list.html'
    login_url='login'

    def get_queryset(self):
        return super().get_queryset().filter(uploaded_by = self.request.user)
    
    
class MyPptSearchResultListView(ListView):
    model = Ppt
    context_object_name = 'ppts'
    template_name="ppts/my_ppt_search_result_list.html"
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Ppt.objects.filter(
            Q(standard__icontains=query) | Q(chapter__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
