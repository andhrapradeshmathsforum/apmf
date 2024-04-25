from django.urls import path
from .views import RpAddView


urlpatterns = [
    path('resource-persons/', RpAddView.as_view(), name='rp_add'),
]
