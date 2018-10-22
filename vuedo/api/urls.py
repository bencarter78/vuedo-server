from django.urls import path

from .views import list

urlpatterns = [
    path('lists', list.index, name='api.lists.index'),
]