from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import News
from django.views.generic import ListView

# Create your views here.
class NewsListView(ListView):
    model = News
    context_object_name = 'news'
    template_name='news/list.html'
    
