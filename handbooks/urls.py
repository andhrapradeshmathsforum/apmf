from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.HandbookAddView.as_view(), name="handbook_add"),
    path('list/', views.HandbookListView.as_view(), name="handbook_list"),
    path('update/<int:pk>/', views.HandbookUpdateView.as_view(), name="handbook_update"),
    path('delete/<int:pk>', views.HandbookDeleteView.as_view(), name="handbook_delete"),    
]