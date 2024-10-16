from django.urls import path
from . import views

urlpatterns = [
    path('', views.quizzes_list, name='quizzes_list'),
]