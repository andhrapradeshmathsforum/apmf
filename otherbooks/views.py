from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import Otherbook
from . forms import OtherbookForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from requestitem.models import Message



# Create your views here.

class OtherbookAddView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    form_class = OtherbookForm
    model = Otherbook
    template_name = "otherbooks/add.html"
    success_url = reverse_lazy('otherbook_list')
    login_url = 'login'
    success_message = "%(title)s  was added successfully" 
   

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    

class OtherbookListView(ListView):
    model = Otherbook
    context_object_name = 'otherbooks'
    template_name="otherbooks/list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = Message.objects.filter(request_for = 'other_book')
        return context
    

class OtherbookUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Otherbook
    template_name = "otherbooks/update.html"
    success_url = reverse_lazy('otherbook_list')
    form_class = OtherbookForm
    login_url='login'
    success_message = "%(title)s was updated successfully" 

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class OtherbookDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = Otherbook
    template_name = "otherbooks/delete.html"
    success_url = reverse_lazy('otherbook_list')
    login_url = 'login'     
    context_object_name = 'otherbook'
    def get_success_message(self, cleaned_data):
        return f'{self.object.title} has been deleted'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

