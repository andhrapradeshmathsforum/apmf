from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.TeachingvideoAddView.as_view(), name="teachingvideo_add"),
    path('list/', views.TeachingvideoListView.as_view(), name="teachingvideo_list"),
    path('update/<int:pk>/', views.TeachingvideoUpdateView.as_view(), name="teachingvideo_update"),
    path('delete/<int:pk>', views.TeachingvideoDeleteView.as_view(), name="teachingvideo_delete"),    
]