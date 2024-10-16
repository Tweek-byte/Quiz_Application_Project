from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from session.models import Profile
from django.db.models import Q
import pandas as p

@login_required
def quizzes_list(request):
    """Logic for showing list of quizzes"""
    quizzes = Quiz.objects.order_by('-created_at')
    categories = Category.objects.all()

    context = {"quizzes": quizzes, "categories": categories}
    return render(request, 'quizzes_list.html', context)

@login_required
def search(request, category):
    """Search quizzes logic"""
    if request.GET.get('q') != None:
        q = request.GET.get('q')
        query = Q(name__icontains=q) | Q(description__icontains=q)
        quizzes = Quiz.objects.filter(query).order_by('-created_at')

    elif category != " ":
        quizzes = Quiz.objects.filter(category__name=category).order_by('-created_at')
    
    else:
        quizzes = Quiz.objects.order_by('-created_at')


    categories = Category.objects.all()

    context = {"quizzes": quizzes, "categories": categories}
    return render(request, 'quizzes_list.html', context)