from django.shortcuts import render
from django.views import generic
from .models import Key
from .forms import KeyForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from requestitem.models import Message


# Create your views here.


class KeyAddView(SuccessMessageMixin, LoginRequiredMixin,  generic.CreateView):
    model = Key
    form_class = KeyForm
    template_name = "keys/add.html"
    login_url = 'login'
    success_url = reverse_lazy('key_list')
    success_message = '%(standard)s class %(exam)s %(year)s %(title)s wad added successfully'
    
    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    



class KeyListView(generic.ListView):
    model = Key
    context_object_name = 'keys'
    template_name='keys/list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = Message.objects.filter(request_for = 'keys')
        return context



class KeyUpdateView(SuccessMessageMixin, LoginRequiredMixin,generic.UpdateView):
    model = Key
    template_name = "keys/update.html"
    form_class = KeyForm
    login_url = 'login'
    success_url = reverse_lazy('key_list')
    success_message = '%(standard)s class %(exam)s %(year)s %(title)s wad updated successfully'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class KeyDeleteView(SuccessMessageMixin, LoginRequiredMixin,generic.DeleteView):
    model = Key
    template_name = "keys/delete.html"
    login_url = 'login'
    context_object_name = 'key'
    success_url = reverse_lazy('key_list')

    def get_success_message(self, cleaned_data: dict[str, str]) -> str:
        return f'{self.object.standard} class {self.object.exam} {self.object.year} {self.object.title} was deleted successfully'
        return super().get_success_message(cleaned_data)
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
    



