from django.urls import path
from .views import SearchResultListView
urlpatterns = [
    path('search-results/', SearchResultListView.as_view(), name='search_result_list'),
]
