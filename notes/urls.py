from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.NotesAddView.as_view(), name="notes_add"),
    path('list/', views.NotesListView.as_view(), name="notes_list"),
    path('update/<int:pk>/', views.NotesUpdateView.as_view(), name="notes_update"),
    path('delete/<int:pk>', views.NotesDeleteView.as_view(), name="notes_delete"),    
]