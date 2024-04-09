from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import Textbook
from . forms import TextbookForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

class TextbookAddView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    form_class = TextbookForm
    model = Textbook
    template_name = "textbooks/add.html"
    success_url = reverse_lazy('textbook_list')
    login_url = 'login'
    success_message = "%(standard)s Class %(semester)s %(title)s was added successfully" 
   

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    

class TextbookListView(ListView):
    model = Textbook
    context_object_name = 'textbooks'
    template_name="textbooks/list.html"
    

class TextbookUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Textbook
    template_name = "textbooks/update.html"
    success_url = reverse_lazy('textbook_list')
    form_class = TextbookForm
    login_url='login'
    success_message = "%(standard)s Class %(semester)s %(title)s was updated successfully" 

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class TextbookDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = Textbook
    template_name = "textbooks/delete.html"
    success_url = reverse_lazy('textbook_list')
    login_url = 'login'     
    context_object_name = 'textbook'
    def get_success_message(self, cleaned_data):
        return f'{self.object.standard} Class {self.object.semester} {self.object.title} has been deleted'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

class TextbookSearchResultListView(ListView):
    model = Textbook
    context_object_name = 'textbooks'
    template_name="textbooks/textbook_search_result_list.html"
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Textbook.objects.filter(
            Q(standard__icontains=query) | Q(semester__icontains=query) |
            Q(title__icontains=query) | Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
    
class MyTextBookListView(LoginRequiredMixin,ListView):
    model = Textbook
    context_object_name = 'textbooks'
    template_name = 'textbooks/my_textbook_list.html'
    login_url='login'

    def get_queryset(self):
        return super().get_queryset().filter(uploaded_by = self.request.user)
    
    
class MyTextbookSearchResultListView(ListView):
    model = Textbook
    context_object_name = 'textbooks'
    template_name="textbooks/my_textbook_search_result_list.html"
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Textbook.objects.filter(
            Q(standard__icontains=query) | Q(semester__icontains=query) |
            Q(title__icontains=query) | Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
