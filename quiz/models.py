"""Quiz Models"""
from django.db import models
import pandas as pd
from django.contrib.auth.models import User
from django.db.models import Sum

class Category(models.Model):
    """Model representing quiz categories (e.g., Science, History)."""
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return (self.name)


class Quiz(models.Model):
    """Model representing a quiz with imported from a file"""
    name = models.CharField(max_length=255, default="Untitled Quiz")
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='quizzes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quiz_f = models.FileField(upload_to='quiz/')

    class Meta:
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return (self.name)

    def save(self, *args, **kwargs):
        """Save the quiz and import questions if a file is uploaded."""
        super().save(*args, **kwargs)
        if self.quiz_f:
            self.quiz_import()

    def quiz_import(self):
        """Import questions from an uploaded Excel file."""
        fd = pd.read_excel(self.quiz_f.path)

        for index, row in fd.iterrows():
            question_txt = row['Question']
            c1 = row['A']
            c2 = row['B']
            c3 = row['C']
            c4 = row['D']
            c5 = row['F']
            answer = row['Answer']


            question_obj, created = Question.objects.get_or_create(quiz=self, text=question_txt)
            print(f"{'Created' if created else 'Found'} Question: {question_txt}")


            choices = [
                (c1, answer == 'A'),
                (c2, answer == 'B'),
                (c3, answer == 'C'),
                (c4, answer == 'D'),
                (c5, answer == 'F'),
            ]

            for choice_text, is_correct in choices:
                if choice_text:
                    choice_obj, created = Choice.objects.get_or_create(question=question_obj, text=choice_text, is_correct=is_correct)
                    print(f"{'Created' if created else 'Found'} Choice: {choice_text} for Question: {question_txt}")


class Question(models.Model):
    """Model representing a question in a quiz."""
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    def __str__(self):
        return (self.text[:50])


class Choice(models.Model):
    """Model representing a choice/answer for a question."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return (f"{self.question.text[:50]} - {self.text[:20]}")

class QuizCompleted(models.Model):
    """Model to track quizzes completed by users."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.user}, {self.quiz.name}")

class ProfileRank(models.Model):
    """Model to maintain user rankings based on total score."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.IntegerField(null=True, blank=True)
    total_score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return (f"{self.rank}, {self.user.username}")
    
    
def update_ranking():
    """Update user rankings based on their total quiz scores."""
    user_scores = (QuizCompleted.objects.values('user').annotate(total_score=Sum('score')).order_by('-total_score'))

    rank = 1
    for entry in user_scores:
        user_id = entry['user']
        total_score = entry['total_score']

        user_rank, created = ProfileRank.objects.get_or_create(user_id=user_id)
        user_rank.rank = rank
        user_rank.total_score = total_score
        user_rank.save()

        rank += 1