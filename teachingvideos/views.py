from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import Teachingvideo
from . forms import TeachingvideoForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from requestitem.models import Message


# Create your views here.

class TeachingvideoAddView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    form_class = TeachingvideoForm
    model = Teachingvideo
    template_name = "teachingvideos/add.html"
    success_url = reverse_lazy('teachingvideo_list')
    login_url = 'login'
    success_message = "%(standard)s class %(title)s video was added successfully" 
   

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    

class TeachingvideoListView(ListView):
    model = Teachingvideo
    context_object_name = "teachingvideos"
    template_name='teachingvideos/list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = Message.objects.filter(request_for = 'teaching_video')
        return context
    

class TeachingvideoUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Teachingvideo
    template_name = "teachingvideos/update.html"
    success_url = reverse_lazy('teachingvideo_list')
    form_class = TeachingvideoForm
    login_url='login'
    success_message = "%(standard)s class %(title)s video was updated successfully" 

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class TeachingvideoDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = Teachingvideo
    template_name = "teachingvideos/delete.html"
    success_url = reverse_lazy('teachingvideo_list')
    login_url = 'login'     
    context_object_name = 'teachingvideo'
    def get_success_message(self, cleaned_data):
        return f'{self.object.standard} class {self.object.title} video has been deleted'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

