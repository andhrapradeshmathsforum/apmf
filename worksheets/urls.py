from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.WorksheetAddView.as_view(), name="worksheet_add"),
    path('list/', views.WorksheetListView.as_view(), name="worksheet_list"),
    path('update/<int:pk>/', views.WorksheetUpdateView.as_view(), name="worksheet_update"),
    path('delete/<int:pk>', views.WorksheetDeleteView.as_view(), name="worksheet_delete"),    
]