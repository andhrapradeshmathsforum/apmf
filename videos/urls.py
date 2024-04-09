from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.VideoAddView.as_view(), name="video_add"),
    path('list/', views.VideoListView.as_view(), name="video_list"),
    path('update/<int:pk>/', views.VideoUpdateView.as_view(), name="video_update"),
    path('delete/<int:pk>', views.VideoDeleteView.as_view(), name="video_delete"),    
]