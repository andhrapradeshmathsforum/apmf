from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.NmmsQuestionpaperAddView.as_view(), name="nmmsQuestionpaper_add"),
    path('list/', views.NmmsQuestionpaperListView.as_view(), name="nmmsQuestionpaper_list"),
    path('update/<int:pk>/', views.NmmsQuestionpaperUpdateView.as_view(), name="nmmsQuestionpaper_update"),
    path('delete/<int:pk>', views.NmmsQuestionpaperDeleteView.as_view(), name="nmmsQuestionpaper_delete"),    
]