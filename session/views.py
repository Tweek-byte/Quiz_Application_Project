from django.shortcuts import render

def register(request):
    context = {}
    return render(request, "register.html", context)
