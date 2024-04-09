from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.PptAddView.as_view(), name="ppt_add"),
    path('list/', views.PptListView.as_view(), name="ppt_list"),
    path('update/<int:pk>/', views.PptUpdateView.as_view(), name="ppt_update"),
    path('delete/<int:pk>', views.PptDeleteView.as_view(), name="ppt_delete"),    
]