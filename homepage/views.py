from django.shortcuts import render

def home(request):
    """Home Page Logic"""
    return render(request, 'homepage.html')