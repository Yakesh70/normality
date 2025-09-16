from django.urls import path
from . import views_simple

urlpatterns = [
    path("", views_simple.analyze_view, name="analyze"),
]
