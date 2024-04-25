from django.shortcuts import render
from . models import Hot
from . forms import HotForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from requestitem.models import Message



# Create your views here.


class HotAddView(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    model = Hot
    form_class = HotForm
    template_name = "hots/add.html"
    login_url = 'login'
    success_url = reverse_lazy('hot_list')
    context_object_name = 'hots'
    success_message = '%(standard)s class %(chapter)s %(title)s was added successfully.'
    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    



class HotListView(generic.ListView):
    model = Hot
    context_object_name = 'hots'
    template_name='hots/list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = Message.objects.filter(request_for = 'hot')
        return context


class HotUpdateView(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    model = Hot
    form_class = HotForm
    template_name = "hots/update.html"
    login_url = 'login'
    success_url = reverse_lazy('hot_list')
    context_object_name ='hot'
    success_message = '%(standard)s class %(chapter)s %(title)s was updated successfully.'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

class HotDeleteView(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView):
    model = Hot
    template_name = "hots/delete.html"
    login_url = 'login'
    success_url =reverse_lazy('hot_list')
    context_object_name = 'hot'
    def get_success_message(self, cleaned_data: dict[str, str]) -> str:
        return f'{self.object.standard} class {self.object.chapter} {self.object.title} was deleted successfully.'










