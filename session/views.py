"""Session Management Logic."""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Profile
from django.contrib.auth.decorators import login_required

def register(request):
    """Signing Up Logic."""
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username already exists! Try Logging in.")
                    return redirect('register')
                
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email already exists! Try Logging in.")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    
                    user_login = auth.authenticate(username=username, password=password)
                    auth.login(request, user_login)


                    user_model = User.objects.get(username=username)
                    new_profile = Profile.objects.create(user=user_model, email_address=email)
                    new_profile.save()
                    return redirect('profile', username)
        else:
            messages.info(request, "Failed to confirm password!")
            return redirect('register')

    context = {}
    return render(request, "register.html", context)


def profile(request, username):
    """Profile Dashboard Logic."""
    user_obj = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=user_obj)
    
    context = {"user_profile": user_profile}
    return (render(request, 'profile.html', context))

def login(request):
    "login Logic."""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return (redirect('profile', username))
        else:
            messages.info(request, 'Invalid username or password!')
            return (redirect('login'))
        
    return (render(request, "login.html"))

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return (redirect('login'))