from django.urls import path
from .views import hello_recruto

urlpatterns = [
    path('', hello_recruto, name='hello_recruto'),
]