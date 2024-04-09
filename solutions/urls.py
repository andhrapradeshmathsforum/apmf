from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.SolutionAddView.as_view(), name="solution_add"),
    path('list/', views.SolutionListView.as_view(), name="solution_list"),
    path('update/<int:pk>/', views.SolutionUpdateView.as_view(), name="solution_update"),
    path('delete/<int:pk>', views.SolutionDeleteView.as_view(), name="solution_delete"),    
]