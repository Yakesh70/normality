from django.urls import path
from . import views_minimal

urlpatterns = [
    path("", views_minimal.analyze_view, name="analyze"),
]
