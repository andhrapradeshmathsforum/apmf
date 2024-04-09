from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.NmmsMaterialAddView.as_view(), name="nmmsMaterial_add"),
    path('list/', views.NmmsMaterialListView.as_view(), name="nmmsMaterial_list"),
    path('update/<int:pk>/', views.NmmsMaterialUpdateView.as_view(), name="nmmsMaterial_update"),
    path('delete/<int:pk>', views.NmmsMaterialDeleteView.as_view(), name="nmmsMaterial_delete"),    
]