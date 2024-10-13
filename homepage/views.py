from django.shortcuts import render, HttpResponse

def home():
    """Home Page Logic"""
    return(HttpResponse("Home Page Created"))
