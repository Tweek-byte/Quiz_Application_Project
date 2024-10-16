from django.shortcuts import render
from .models import Quiz

def quizzes_list(request):
    quizzes = Quiz.objects.select_related('category').order_by('-created_at')
    return render(request, 'quizzes_list.html', {'quizzes': quizzes})