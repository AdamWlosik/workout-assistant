from django.urls import path

from . import views

urlpatterns = [
    path("", views.exercises_list, name="exercises"),
    path("<int:exercise_id>/", views.exercise_detail, name="exercise_detail"),
    path("create/", views.exercise_create, name="exercise_create"),
    path("<int:exercise_id>/edit/", views.exercise_edit, name="exercise_edit"),
    path("<int:exercise_id>/delete/", views.exercise_delete, name="exercise_delete"),
]
