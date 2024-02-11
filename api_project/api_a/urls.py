from django.urls import path
from .views import sum_view

urlpatterns = [
    path('sum/', sum_view, name='sum_view'),
]
