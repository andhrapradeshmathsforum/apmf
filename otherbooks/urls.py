from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.OtherbookAddView.as_view(), name="otherbook_add"),
    path('list/', views.OtherbookListView.as_view(), name="otherbook_list"),
    path('update/<int:pk>/', views.OtherbookUpdateView.as_view(), name="otherbook_update"),
    path('delete/<int:pk>', views.OtherbookDeleteView.as_view(), name="otherbook_delete"),    
]