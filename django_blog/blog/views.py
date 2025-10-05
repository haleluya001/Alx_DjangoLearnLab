# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib import messages

def register_view(request):
    if request.user.is_authenticated:
        return redirect('blog:profile')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Auto-login after registration (optional)
            login(request, user)
            messages.success(request, "Registration successful. You're now logged in.")
            return redirect('blog:profile')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile_view(request):
    # Show and edit profile
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('blog:profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'blog/profile.html', {'form': form})


from django.shortcuts import render

def home_view(request):
    return render(request, 'blog/home.html')