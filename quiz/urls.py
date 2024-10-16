from django.urls import path
from . import views

urlpatterns = [
    path('', views.quizzes_list, name='quizzes_list'),
    path('take', views.quiz_page, name='quiz_page'),
    path('search/<str:category>', views.search, name='search'),
    path('<int:quiz_id>/', views.quiz_page, name='quiz'),
    path('result/<int:submission_id>/', views.quiz_result, name='quiz_result')
]