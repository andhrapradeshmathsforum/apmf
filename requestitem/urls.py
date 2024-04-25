from django.urls import path
from .views import MessageAddView

urlpatterns = [
    path('request_an_item/', MessageAddView.as_view(), name='request_item'),
]
