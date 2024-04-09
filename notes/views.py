from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import Notes
from . forms import NotesForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

class NotesAddView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    form_class = NotesForm
    model = Notes
    template_name = "notes/add.html"
    success_url = reverse_lazy('notes_list')
    login_url = 'login'
    success_message = "%(standard)s Class %(chapter)s notes was added successfully" 
   

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    

class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name="notes/list.html"
    

class NotesUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Notes
    template_name = "notes/update.html"
    success_url = reverse_lazy('notes_list')
    form_class = NotesForm
    login_url='login'
    success_message = "%(standard)s Class %(chapter)s notes was updated successfully" 

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class NotesDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = Notes
    template_name = "notes/delete.html"
    success_url = reverse_lazy('notes_list')
    login_url = 'login'     
    context_object_name = 'note'
    def get_success_message(self, cleaned_data):
        return f'{self.object.standard} Class {self.object.chapter}  notes has been deleted'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

class NotesSearchResultListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name="notes/notes_search_result_list.html"
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Notes.objects.filter(
            Q(standard__icontains=query) | Q(chapter__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
    
class MyNotesListView(LoginRequiredMixin,ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/my_list.html'
    login_url='login'

    def get_queryset(self):
        return super().get_queryset().filter(uploaded_by = self.request.user)
    
    
class MyNotesSearchResultListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name="notess/my_notes_search_result_list.html"
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Notes.objects.filter(
            Q(standard__icontains=query) |
            Q(chapter__icontains=query) | Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
