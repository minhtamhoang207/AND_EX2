from django.urls import path
from .view import country

urlpatterns = [
    path('country/', country, name="countries")
]