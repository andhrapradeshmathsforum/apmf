from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import Video
from . forms import VideoForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class VideoAddView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    form_class = VideoForm
    model = Video
    template_name = "videos/add.html"
    success_url = reverse_lazy('video_list')
    login_url = 'login'
    success_message = "%(title)s video was added successfully" 
   

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    

class VideoListView(ListView):
    model = Video
    context_object_name = "videos"
    template_name='videos/list.html'
    

class VideoUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Video
    template_name = "videos/update.html"
    success_url = reverse_lazy('video_list')
    form_class = VideoForm
    login_url='login'
    success_message = "%(title)s video was updated successfully" 

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class VideoDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    model = Video
    template_name = "videos/delete.html"
    success_url = reverse_lazy('video_list')
    login_url = 'login'     
    context_object_name = 'video'
    def get_success_message(self, cleaned_data):
        return f'{self.object.title} video has been deleted'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

