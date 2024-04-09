from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.ExamplarmathAddView.as_view(), name="examplarmath_add"),
    path('list/', views.ExamplarmathListView.as_view(), name="examplarmath_list"),
    path('update/<int:pk>/', views.ExamplarmathUpdateView.as_view(), name="examplarmath_update"),
    path('delete/<int:pk>', views.ExamplarmathDeleteView.as_view(), name="examplarmath_delete"),    
]