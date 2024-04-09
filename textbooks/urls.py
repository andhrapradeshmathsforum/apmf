from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.TextbookAddView.as_view(), name="textbook_add"),
    path('list/', views.TextbookListView.as_view(), name="textbook_list"),
    path('update/<int:pk>/', views.TextbookUpdateView.as_view(), name="textbook_update"),
    path('delete/<int:pk>', views.TextbookDeleteView.as_view(), name="textbook_delete"),    
]