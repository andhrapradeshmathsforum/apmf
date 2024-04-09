from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import Project
from . forms import ProjectForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

class ProjectAddView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    form_class = ProjectForm
    model = Project
    template_name = "projects/add.html"
    success_url = reverse_lazy('project_list')
    login_url = 'login'
    success_message = "%(standard)s Class %(exam)s %(chapter)s was added successfully" 
   

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    

class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name="projects/list.html"
    

class ProjectUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Project
    template_name = "projects/update.html"
    success_url = reverse_lazy('project_list')
    form_class = ProjectForm
    login_url='login'
    success_message = "%(standard)s Class %(exam)s %(chapter)s was updated successfully" 

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class ProjectDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = Project
    template_name = "projects/delete.html"
    success_url = reverse_lazy('project_list')
    login_url = 'login'     
    context_object_name = 'project'
    def get_success_message(self, cleaned_data):
        return f'{self.object.standard} Class {self.object.exam} {self.object.chapter}  has been deleted'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

class ProjectSearchResultListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name="projects/project_search_result_list.html"
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Project.objects.filter(
            Q(standard__icontains=query) | Q(chapter__icontains=query) |
            Q(uploaded_by__name__icontains=query) | Q(exam__icontains=query) |
            Q(description__icontains=query)  
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
    
class MyProjectListView(LoginRequiredMixin,ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/my_list.html'
    login_url='login'

    def get_queryset(self):
        return super().get_queryset().filter(uploaded_by = self.request.user)
    
    
class MyProjectSearchResultListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name="projectss/my_projects_search_result_list.html"
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Project.objects.filter(
            Q(standard__icontains=query) | Q(exam__icontains=query) |
            Q(chapter__icontains=query) | Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
