from django.urls import path
from homepage import views
"""Homepage link."""

urlpatterns = [
    path('', views.home, name='homepage'),
]