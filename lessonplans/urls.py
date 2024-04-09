from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.LessonplanAddView.as_view(), name="lessonplan_add"),
    path('list/', views.LessonplanListView.as_view(), name="lessonplan_list"),
    path('update/<int:pk>/', views.LessonplanUpdateView.as_view(), name="lessonplan_update"),
    path('delete/<int:pk>', views.LessonplanDeleteView.as_view(), name="lessonplan_delete"),    
]