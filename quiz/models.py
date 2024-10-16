"""Quiz Models"""
from django.db import models

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

    class Meta:
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    def __str__(self):
        return self.text[:50]


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    isCorrect = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.text[:50]} - {self.text[:20]}"
