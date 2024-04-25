from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.QuizAddView.as_view(), name="quiz_add"),
    path('list/', views.QuizListView.as_view(), name="quiz_list"),
    path('update/<int:pk>/', views.QuizUpdateView.as_view(), name="quiz_update"),
    path('delete/<int:pk>', views.QuizDeleteView.as_view(), name="quiz_delete"),    
]