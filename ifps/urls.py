from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.IfpAddView.as_view(), name="ifp_add"),
    path('list/', views.IfpListView.as_view(), name="ifp_list"),
    path('update/<int:pk>/', views.IfpUpdateView.as_view(), name="ifp_update"),
    path('delete/<int:pk>', views.IfpDeleteView.as_view(), name="ifp_delete"),    
]