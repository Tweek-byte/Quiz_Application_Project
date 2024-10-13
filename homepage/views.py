from django.shortcuts import render, HttpResponse

def home(request):
    """Home Page Logic"""
    render(request, 'index.html')
