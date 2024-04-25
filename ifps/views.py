from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import Ifp
from . forms import IfpForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from requestitem.models import Message


# Create your views here.

class IfpAddView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    form_class = IfpForm
    model = Ifp
    template_name = "ifps/add.html"
    success_url = reverse_lazy('ifp_list')
    login_url = 'login'
    success_message = "%(title)s video was added successfully" 
   

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    

class IfpListView(ListView):
    model = Ifp
    context_object_name = "ifps"
    template_name='ifps/list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = Message.objects.filter(request_for = 'ifp_usage')
        return context
    

class IfpUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Ifp
    template_name = "ifps/update.html"
    success_url = reverse_lazy('ifp_list')
    form_class = IfpForm
    login_url='login'
    success_message = "%(title)s video was updated successfully" 

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class IfpDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = Ifp
    template_name = "ifps/delete.html"
    success_url = reverse_lazy('ifp_list')
    login_url = 'login'     
    context_object_name = 'ifp'
    def get_success_message(self, cleaned_data):
        return f'{self.object.title} video has been deleted'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

