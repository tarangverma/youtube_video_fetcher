from django.urls import path
from . import views

urlpatterns = [
    path("videos/", views.get_videos, name="get_videos"),
    path("template/", views.dashboard_view, name="dashboard_view"),
]
