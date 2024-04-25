from django.shortcuts import render
from . models import Mindmap
from . forms import MindmapForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from requestitem.models import Message



# Create your views here.


class MindmapAddView(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    model = Mindmap
    form_class = MindmapForm
    template_name = "mindmaps/add.html"
    login_url = 'login'
    success_url = reverse_lazy('mindmap_list')
    context_object_name = 'mindmaps'
    success_message = '%(standard)s class %(chapter)s %(title)s was added successfully.'
    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    



class MindmapListView(generic.ListView):
    model = Mindmap
    context_object_name = 'mindmaps'
    template_name='mindmaps/list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = Message.objects.filter(request_for = 'mind_maps')
        return context


class MindmapUpdateView(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    model = Mindmap
    form_class = MindmapForm
    template_name = "mindmaps/update.html"
    login_url = 'login'
    success_url = reverse_lazy('mindmap_list')
    context_object_name ='mindmap'
    success_message = '%(standard)s class %(chapter)s %(title)s was updated successfully.'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

class MindmapDeleteView(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView):
    model = Mindmap
    template_name = "mindmaps/delete.html"
    login_url = 'login'
    success_url =reverse_lazy('mindmap_list')
    context_object_name = 'mindmap'
    def get_success_message(self, cleaned_data: dict[str, str]) -> str:
        return f'{self.object.standard} class {self.object.chapter} {self.object.title} was deleted successfully.'










