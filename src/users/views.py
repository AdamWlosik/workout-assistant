from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile


class SignUp(generic.CreateView):
    """Class to display signup view"""

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "users/signup.html"


@login_required
def edit_profile(request: HttpRequest) -> HttpResponse:
    """Function to display edit profile view"""
    user = request.user
    profile, _ = Profile.objects.get_or_create(user=user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile_view")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "users/edit_profile.html", {"form": form})


@login_required
def profile_view(request: HttpRequest) -> HttpResponse:
    """Function to display user profile view"""
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, "users/profile_view.html", {"profile": profile})
