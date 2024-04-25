from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.HotAddView.as_view(), name='hot_add'),
    path('list/', views.HotListView.as_view(), name = 'hot_list'),
    path('update/<int:pk>/', views.HotUpdateView.as_view(), name = 'hot_update'),
    path('delete/<int:pk>/', views.HotDeleteView.as_view(), name = 'hot_delete'),
]
