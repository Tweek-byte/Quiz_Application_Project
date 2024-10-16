from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, Category, QuizCompleted
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def quizzes_list(request):
    """Logic for showing list of quizzes."""
    quizzes = Quiz.objects.order_by('-created_at')
    categories = Category.objects.all()

    context = {"quizzes": quizzes, "categories": categories}
    return render(request, 'quizzes_list.html', context)

@login_required
def search(request, category):
    """Search quizzes logic."""
    q = request.GET.get('q')
    
    if q:
        query = Q(name__icontains=q) | Q(description__icontains=q)
        quizzes = Quiz.objects.filter(query).order_by('-created_at')
    elif category != " ":
        quizzes = Quiz.objects.filter(category__name=category).order_by('-created_at')
    else:
        quizzes = Quiz.objects.order_by('-created_at')

    categories = Category.objects.all()
    context = {"quizzes": quizzes, "categories": categories}
    return render(request, 'quizzes_list.html', context)

@login_required
def quiz_page(request, quiz_id):
    """Logic for displaying a quiz page."""
    quiz = get_object_or_404(Quiz, pk=quiz_id)

    if request.method == "POST":
        score = int(request.POST.get('score', 0))
        submission = QuizCompleted(user=request.user, quiz=quiz, score=score)
        submission.save()
        return redirect('quiz_result', submission_id=submission.id)

    return render(request, 'quiz_page.html', {'quiz': quiz})

@login_required
def quiz_result(request, submission_id):
    """View to display quiz results."""
    submission = get_object_or_404(QuizCompleted, id=submission_id)
    total_questions = submission.quiz.questions.count()

    context = {
        'submission': submission,
        'total_questions': total_questions,
        'correct_answers': submission.score,
        'incorrect_answers': total_questions - submission.score
    }
    return render(request, 'quiz_result.html', context)
