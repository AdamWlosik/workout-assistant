from django.urls import path

from . import views, hx_views

urlpatterns = [
    path("", views.trainings_list, name="trainings"),
    path("<int:training_id>/", views.training_detail, name="training_detail"),
    path("create/", views.training_create, name="training_create"),
    path("<int:training_id>/edit/", views.training_edit, name="training_edit"),
    path("<int:training_id>/delete/", views.training_delete, name="training_delete"),
]
urlpatterns += [
    path(
        "<int:training_id>/hx-training-exercise-add", hx_views.hx_training_exercise_add, name="hx-training-exercise-add"
    )
]
