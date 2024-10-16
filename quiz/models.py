from django.db import models

class Category(models.Model):
    """Quiz Category model"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    """Quiz model"""
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='quizzes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

