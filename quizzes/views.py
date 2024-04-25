from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import Quiz
from . forms import QuizForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from requestitem.models import Message



# Create your views here.

class QuizAddView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    form_class = QuizForm
    model = Quiz
    template_name = "quizzes/add.html"
    success_url = reverse_lazy('quiz_list')
    login_url = 'login'
    success_message =  "Quiz : ' %(standard)s Class %(topic)s %(sub_topic)s ' was added successfully" 
   

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    

class QuizListView(ListView):
    model = Quiz
    context_object_name = 'quizs'
    template_name="quizzes/list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = Message.objects.filter(request_for = 'quiz')
        return context
    

class QuizUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Quiz
    template_name = "quizzes/update.html"
    success_url = reverse_lazy('quiz_list')
    form_class = QuizForm
    login_url='login'
    success_message =  "Quiz : ' %(standard)s Class %(topic)s %(sub_topic)s ' was added successfully" 
   

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class QuizDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = Quiz
    template_name = "quizzes/delete.html"
    success_url = reverse_lazy('quiz_list')
    login_url = 'login'     
    context_object_name = 'quiz'
    def get_success_message(self, cleaned_data):
        return f"'{self.object.standard} Class {self.object.topic} {self.object.sub_topic}' has been deleted"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

