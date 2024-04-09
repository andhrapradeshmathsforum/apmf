from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import Solution
from . forms import SolutionForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

class SolutionAddView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    form_class = SolutionForm
    model = Solution
    template_name = "solutions/add.html"
    success_url = reverse_lazy('solution_list')
    login_url = 'login'
    success_message = "%(standard)s Class %(chapter)s solutions were added successfully" 
   

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    

class SolutionListView(ListView):
    model = Solution
    context_object_name = 'solutions'
    template_name="solutions/list.html"
    

class SolutionUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Solution
    template_name = "solutions/update.html"
    success_url = reverse_lazy('solution_list')
    form_class = SolutionForm
    login_url='login'
    success_message = "%(standard)s Class %(chapter)s solutions were updated successfully" 

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class SolutionDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = Solution
    template_name = "solutions/delete.html"
    success_url = reverse_lazy('solution_list')
    login_url = 'login'    
    context_object_name = 'solution' 
    def get_success_message(self, cleaned_data):
        return f'{self.object.standard} Class {self.object.chapter} solutions were been deleted'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

class SolutionSearchResultListView(ListView):
    model = Solution
    context_object_name = 'solutions'
    template_name="solutions/solution_search_result_list.html"
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Solution.objects.filter(
            Q(standard__icontains=query) | Q(chapter__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
    
class MySolutionListView(LoginRequiredMixin,ListView):
    model = Solution
    context_object_name = 'solutions'
    template_name = 'solutions/my_solution_list.html'
    login_url='login'

    def get_queryset(self):
        return super().get_queryset().filter(uploaded_by = self.request.user)
    
    
class MySolutionSearchResultListView(ListView):
    model = Solution
    context_object_name = 'solutions'
    template_name="solutions/my_solution_search_result_list.html"
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Solution.objects.filter(
            Q(standard__icontains=query) | Q(semester__icontains=query) |
            Q(title__icontains=query) | Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
