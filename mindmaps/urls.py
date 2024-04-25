from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.MindmapAddView.as_view(), name='mindmap_add'),
    path('list/', views.MindmapListView.as_view(), name = 'mindmap_list'),
    path('update/<int:pk>/', views.MindmapUpdateView.as_view(), name = 'mindmap_update'),
    path('delete/<int:pk>/', views.MindmapDeleteView.as_view(), name = 'mindmap_delete'),
]
