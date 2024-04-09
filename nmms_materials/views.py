from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import NmmsMaterial
from . forms import NmmsMaterialForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

class NmmsMaterialAddView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    form_class = NmmsMaterialForm
    model = NmmsMaterial
    template_name = "nmms_materials/add.html"
    success_url = reverse_lazy('nmmsMaterial_list')
    login_url = 'login'
    success_message = "%(title)s was added successfully" 
   

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    

class NmmsMaterialListView(ListView):
    model = NmmsMaterial
    context_object_name = 'nmmsMaterials'
    template_name="nmms_materials/list.html"
    

class NmmsMaterialUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = NmmsMaterial
    template_name = "nmms_materials/update.html"
    success_url = reverse_lazy('nmmsMaterial_list')
    form_class = NmmsMaterialForm
    login_url='login'
    success_message = "%(title)s was updated successfully" 

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class NmmsMaterialDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = NmmsMaterial
    template_name = "nmms_materials/delete.html"
    success_url = reverse_lazy('nmmsMaterial_list')
    login_url = 'login'     
    context_object_name = 'nmmsMaterial'
    def get_success_message(self, cleaned_data):
        return f'{self.object.chapter} has been deleted'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

class NmmsMaterialSearchResultListView(ListView):
    model = NmmsMaterial
    context_object_name = 'nmmsMaterials'
    template_name="nmms_materials/nmms_material_search_result_list.html"
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return NmmsMaterial.objects.filter(           
            Q(title__icontains=query) | Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
    
class MyNmmsMaterialListView(LoginRequiredMixin,ListView):
    model = NmmsMaterial
    context_object_name = 'nmmsMaterials'
    template_name = 'nmms_materials/my_nmms_materials_list.html'
    login_url='login'

    def get_queryset(self):
        return super().get_queryset().filter(uploaded_by = self.request.user)
    
    
class MyNmmsMaterialSearchResultListView(ListView):
    model = NmmsMaterial
    context_object_name = 'nmmsMaterials'
    template_name="nmms_materials/my_nmms_material_search_result_list.html"
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return NmmsMaterial.objects.filter(
            Q(title__icontains=query) | Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
