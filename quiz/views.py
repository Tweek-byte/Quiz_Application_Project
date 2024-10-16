from django.shortcuts import render
from .models import Quiz, Category
from django.contrib.auth.decorators import login_required

@login_required
def quizzes_list(request):
    """Logic for showing list of quizzes"""
    quizzes = Quiz.objects.order_by('-created_at')
    categories = Category.objects.all()

    context = {"quizzes": quizzes, "categories": categories}
    return render(request, 'quizzes_list.html', context)

@login_required
def search(request):
    """Logic for quizzes list search function"""
    context={
        
    }
    return (render(request, 'quizzes_list.html', context))