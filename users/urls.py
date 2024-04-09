from django.urls import path
from .views import SignUpView
from django.views.generic import TemplateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout_confirm/', TemplateView.as_view(template_name='users/logout_confirm.html'), name='logout_confirm'),
    
]
