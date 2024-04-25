from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.LabAddView.as_view(), name="lab_add"),
    path('list/', views.LabListView.as_view(), name="lab_list"),
    path('update/<int:pk>/', views.LabUpdateView.as_view(), name="lab_update"),
    path('delete/<int:pk>', views.LabDeleteView.as_view(), name="lab_delete"),    
]