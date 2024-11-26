from django.urls import path
from .views import get_conjugations

urlpatterns = [
    path("conjugate/", get_conjugations, name="conjugate"),
]
