from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import Questionpaper
from . forms import QuestionpaperForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

class QuestionpaperAddView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    form_class = QuestionpaperForm
    model = Questionpaper
    template_name = "questionpapers/add.html"
    success_url = reverse_lazy('questionpaper_list')
    login_url = 'login'
    success_message = "%(standard)s Class %(exam)s questionpaper was added successfully" 
   

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    

class QuestionpaperListView(ListView):
    model = Questionpaper
    context_object_name = "questionpapers"
    template_name='questionpapers/list.html'
    

class QuestionpaperUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Questionpaper
    template_name = "questionpapers/update.html"
    success_url = reverse_lazy('questionpaper_list')
    form_class = QuestionpaperForm
    login_url='login'
    success_message = "%(standard)s Class %(exam)s questionpaper was updated successfully" 

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class QuestionpaperDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = Questionpaper
    template_name = "questionpapers/delete.html"
    success_url = reverse_lazy('questionpaper_list')
    login_url = 'login'     
    context_object_name = 'questionpaper'
    def get_success_message(self, cleaned_data):
        return f'{self.object.standard} Class {self.object.exam} questionpaper has been deleted'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

class QuestionpaperSearchResultListView(ListView):
    model = Questionpaper
    context_object_name = "questionpapers"
    template_name="questionpapers/questionpaper_search_result_list.html"
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Questionpaper.objects.filter(
            Q(standard__icontains=query) | Q(exam__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
    
class MyQuestionpaperListView(LoginRequiredMixin,ListView):
    model = Questionpaper
    context_object_name = 'questionpapers'
    template_name = 'questionpapers/my_questionpaper_list.html'
    login_url='login'

    def get_queryset(self):
        return super().get_queryset().filter(uploaded_by = self.request.user)
    
    
class MyQuestionpaperSearchResultListView(ListView):
    model = Questionpaper
    context_object_name = 'questionpapers'
    template_name="questionpapers/my_questionpaper_search_result_list.html"
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Questionpaper.objects.filter(
            Q(standard__icontains=query) | Q(exam__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
