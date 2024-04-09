from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import Lessonplan
from . forms import LessonplanForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

class LessonplanAddView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    form_class = LessonplanForm
    model = Lessonplan
    template_name = "lessonplans/add.html"
    success_url = reverse_lazy('lessonplan_list')
    login_url = 'login'
    success_message = "%(standard)s Class %(chapter)s was added successfully" 
   

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    

class LessonplanListView(ListView):
    model = Lessonplan
    context_object_name = 'lessonplans'
    template_name="lessonplans/list.html"
    

class LessonplanUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Lessonplan
    template_name = "lessonplans/update.html"
    success_url = reverse_lazy('lessonplan_list')
    form_class = LessonplanForm
    login_url='login'
    success_message = "%(standard)s Class %(chapter)s was updated successfully" 

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class LessonplanDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = Lessonplan
    template_name = "lessonplans/delete.html"
    success_url = reverse_lazy('lessonplan_list')
    login_url = 'login'     
    context_object_name ='lessonplan'
    def get_success_message(self, cleaned_data):
        return f'{self.object.standard} Class {self.object.chapter}  has been deleted'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

class LessonplanSearchResultListView(ListView):
    model = Lessonplan
    context_object_name = 'lessonplans'
    template_name="lessonplans/lessonplan_search_result_list.html"
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Lessonplan.objects.filter(
            Q(standard__icontains=query) | Q(chapter__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
    
class MyLessonplanListView(LoginRequiredMixin,ListView):
    model = Lessonplan
    context_object_name = 'lessonplans'
    template_name = 'lessonplans/my_list.html'
    login_url='login'

    def get_queryset(self):
        return super().get_queryset().filter(uploaded_by = self.request.user)
    
    
class MyLessonplanSearchResultListView(ListView):
    model = Lessonplan
    context_object_name = 'lessonplans'
    template_name="lessonplanss/my_lessonplan_search_result_list.html"
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Lessonplan.objects.filter(
            Q(standard__icontains=query) |
            Q(chapter__icontains=query) | Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
