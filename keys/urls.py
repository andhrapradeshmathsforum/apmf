from . import views
from django.urls import path


urlpatterns = [
    path('add/', views.KeyAddView.as_view(), name = 'key_add'),
    path('list/', views.KeyListView.as_view(), name = 'key_list'),
    path('update/<int:pk>/', views.KeyUpdateView.as_view(), name='key_update'),
    path('delete/<int:pk>/', views.KeyDeleteView.as_view(), name ='key_delete'),
]
