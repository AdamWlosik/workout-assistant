from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("profile/", views.profile_view, name="profile_view"),
]
