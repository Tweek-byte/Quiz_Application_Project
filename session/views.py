"""Session Management Logic."""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from .models import Profile
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from quiz.models import ProfileRank

def register(request):
    """Register Logic"""
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

                Profile.objects.create(user=user, email_address=email, age=None, gender=None)

                return redirect('profile', username=username)
        else:
            messages.info(request, "Passwords do not match!")
            return redirect('register')

    return render(request, "register.html")

@login_required
def profile(request, username):
    """Profile Dashboard"""
    user_obj = get_object_or_404(User, username=username)

    user_profile, created = Profile.objects.get_or_create(user=user_obj)

    user_rank = ProfileRank.objects.filter(user=user_obj).first()

    context = {
        'user_profile': user_profile,
        'user_obj': user_obj,
        'user_rank': user_rank,
    }
    return render(request, 'profile.html', context)

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

@login_required
def logout(request):
    """Logging out Logic"""
    auth.logout(request)
    return (redirect('login'))

@login_required
def edit_profile(request, username):
    """Edit Profile Logic"""
    user_profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        username = request.POST.get('username', request.user.username)
        if username != request.user.username:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken!")
                return redirect('edit_profile', username=request.user.username)
            request.user.username = username

        old_password = request.POST.get('old_password')
        new_password = request.POST.get('password')
        if old_password and new_password:
            if check_password(old_password, request.user.password):
                request.user.set_password(new_password)
                update_session_auth_hash(request, request.user)
            else:
                messages.error(request, "Old password is incorrect!")
                return redirect('edit_profile', username=request.user.username)

        if request.FILES.get('profile_img'):
            user_profile.profile_img = request.FILES['profile_img']

        user_profile.age = request.POST.get('age', user_profile.age)
        user_profile.gender = request.POST.get('gender', user_profile.gender)

        request.user.save()
        user_profile.save()

        messages.success(request, "Profile updated successfully!")
        return redirect('profile', username=request.user.username)

    return render(request, 'edit_profile.html', {"user_profile": user_profile})


@login_required
def delete_profile(request, username):
    """Account Deletion Confirmation Logic."""
    user = get_object_or_404(User, username=username)

    if request.method == "POST":

        user = request.user
        user.delete()
        messages.success(request, "Your account has been deleted successfully.")

        logout(request)
        return redirect('register')

    return render(request, 'delete_profile.html')
