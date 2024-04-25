from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import Lab
from . forms import LabForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from requestitem.models import Message



# Create your views here.

class LabAddView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    form_class = LabForm
    model = Lab
    template_name = "labs/add.html"
    success_url = reverse_lazy('lab_list')
    login_url = 'login'
    success_message = "%(standard)s class %(title)s  was added successfully"    

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    

class LabListView(ListView):
    model = Lab
    context_object_name = 'labs'
    template_name="labs/list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = Message.objects.filter(request_for = 'lab_manuals')
        return context
    

class LabUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Lab
    template_name = "labs/update.html"
    success_url = reverse_lazy('lab_list')
    form_class = LabForm
    login_url='login'
    success_message = "%(standard)s class %(title)s was updated successfully" 

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class LabDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = Lab
    template_name = "labs/delete.html"
    success_url = reverse_lazy('lab_list')
    login_url = 'login'     
    context_object_name = 'lab'
    def get_success_message(self, cleaned_data):
        return f'{self.object.standard} class {self.object.title} has been deleted'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

