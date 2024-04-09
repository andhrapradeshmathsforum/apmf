from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.McqAddView.as_view(), name="mcq_add"),
    path('list/', views.McqListView.as_view(), name="mcq_list"),
    path('update/<int:pk>/', views.McqUpdateView.as_view(), name="mcq_update"),
    path('delete/<int:pk>', views.McqDeleteView.as_view(), name="mcq_delete"),    
]