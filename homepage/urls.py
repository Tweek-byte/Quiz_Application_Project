from django.urls import path
from homepage import views
"""Home Page link"""

urlpatterns = [
    path('', views.home, name='homepage'),
]