from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.TlmAddView.as_view(), name = 'tlm_add'),
    path('list/', views.TlmListView.as_view(), name='tlm_list'),
    path('update/<int:pk>/', views.TlmUpdateView.as_view(), name='tlm_update'),
    path('delete/<int:pk>', views.TlmDeleteView.as_view(), name = 'tlm_delete'),
    path('details/<int:pk>/', views.TlmDetailView.as_view(), name='tlm_details')
]
