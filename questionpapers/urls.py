from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.QuestionpaperAddView.as_view(), name="questionpaper_add"),
    path('list/', views.QuestionpaperListView.as_view(), name="questionpaper_list"),
    path('update/<int:pk>/', views.QuestionpaperUpdateView.as_view(), name="questionpaper_update"),
    path('delete/<int:pk>', views.QuestionpaperDeleteView.as_view(), name="questionpaper_delete"),    
]