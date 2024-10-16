"""Quiz Models"""
from django.db import models
import pandas as pd
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Quiz(models.Model):
    name = models.CharField(max_length=255, default="Untitled Quiz")
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='quizzes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quiz_f = models.FileField(upload_to='quiz/')

    class Meta:
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.quiz_f:
            self.quiz_import()

    def quiz_import(self):
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
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    def __str__(self):
        return self.text[:50]


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.text[:50]} - {self.text[:20]}"

class QuizCompleted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}, {self.quiz.name}"

class ProfileRank(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.IntegerField(null=True, blank=True)
    total_score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.rank}, {self.user.username}"