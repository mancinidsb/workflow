# api_rest/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # A rota '' refere-se à página inicial.
]
