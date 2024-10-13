from django.shortcuts import render, HttpResponse

def home(request):
    """Home Page Logic"""
    return(HttpResponse("Home Page Created"))
