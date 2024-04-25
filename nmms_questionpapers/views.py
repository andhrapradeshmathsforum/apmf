from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import NmmsQuestionpaper
from . forms import NmmsQuestionpaperForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from requestitem.models import Message



# Create your views here.

class NmmsQuestionpaperAddView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    form_class = NmmsQuestionpaperForm
    model = NmmsQuestionpaper
    template_name = "nmms_questionpapers/add.html"
    success_url = reverse_lazy('nmmsQuestionpaper_list')
    login_url = 'login'
    success_message = "%(title)s was added successfully" 
   

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    

class NmmsQuestionpaperListView(ListView):
    model = NmmsQuestionpaper
    context_object_name = 'nmmsQuestionpapers'
    template_name="nmms_questionpapers/list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = Message.objects.filter(request_for = 'nmms_question_paper')
        return context
    

class NmmsQuestionpaperUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = NmmsQuestionpaper
    template_name = "nmms_questionpapers/update.html"
    success_url = reverse_lazy('nmmsQuestionpaper_list')
    form_class = NmmsQuestionpaperForm
    login_url='login'
    success_message = "%(title)s was updated successfully" 

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class NmmsQuestionpaperDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = NmmsQuestionpaper
    template_name = "nmms_questionpapers/delete.html"
    success_url = reverse_lazy('nmmsQuestionpaper_list')
    login_url = 'login'     
    context_object_name = 'nmmsQuestionpaper'
    def get_success_message(self, cleaned_data):
        return f'{self.object.title} has been deleted'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

class NmmsQuestionpaperSearchResultListView(ListView):
    model = NmmsQuestionpaper
    context_object_name = 'nmmsQuestionpapers'
    template_name="nmms_questionpapers/nmms_questionpaper_search_result_list.html"
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return NmmsQuestionpaper.objects.filter(           
            Q(title__icontains=query) | Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
    
class MyNmmsQuestionpaperListView(LoginRequiredMixin,ListView):
    model = NmmsQuestionpaper
    context_object_name = 'nmmsQuestionpapers'
    template_name = 'nmms_questionpapers/my_nmms_questionpapers_list.html'
    login_url='login'

    def get_queryset(self):
        return super().get_queryset().filter(uploaded_by = self.request.user)
    
    
class MyNmmsQuestionpaperSearchResultListView(ListView):
    model = NmmsQuestionpaper
    context_object_name = 'nmmsQuestionpapers'
    template_name="nmms_questionpapers/my_nmms_questionpaper_search_result_list.html"
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return NmmsQuestionpaper.objects.filter(
            Q(title__icontains=query) | Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
