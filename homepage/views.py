from django.shortcuts import render

def home(request):
    """Homepage logic."""
    return (render(request, 'homepage.html'))