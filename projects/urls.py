from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.ProjectAddView.as_view(), name="project_add"),
    path('list/', views.ProjectListView.as_view(), name="project_list"),
    path('update/<int:pk>/', views.ProjectUpdateView.as_view(), name="project_update"),
    path('delete/<int:pk>', views.ProjectDeleteView.as_view(), name="project_delete"),    
]