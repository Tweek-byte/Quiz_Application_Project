from django.urls import path
from . import views

urlpatterns = [
    path('quizzes_list', views.quizzes_list, name='quizzes_list'),
    path('search/<str:category>', views.search, name='search'),
]