from django.shortcuts import render
from .models import Member
from django.views.generic import ListView

# Create your views here.


class MemberListView(ListView):
    model = Member
    template_name = "members/list.html"
    context_object_name = 'members'

