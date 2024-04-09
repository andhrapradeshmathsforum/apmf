from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.IctAddView.as_view(), name="ict_add"),
    path('list/', views.IctListView.as_view(), name="ict_list"),
    path('update/<int:pk>/', views.IctUpdateView.as_view(), name="ict_update"),
    path('delete/<int:pk>', views.IctDeleteView.as_view(), name="ict_delete"),    
]