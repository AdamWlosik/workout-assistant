from django.urls import path

from . import hx_views, views

urlpatterns = [
    path("", views.trainings_list, name="trainings"),
    path("<int:training_id>/", views.training_detail, name="training_detail"),
    path("create/", views.training_create, name="training_create"),
    path("<int:training_id>/edit/", views.training_edit, name="training_edit"),
    path("<int:training_id>/delete/", views.training_delete, name="training_delete"),
]
urlpatterns += [
    path(
        "<int:training_id>/hx-training-exercise-list",
        hx_views.hx_training_exercise_list,
        name="hx-training-exercise-list",
    ),
    path(
        "<int:training_id>/hx-training-exercise-add", hx_views.hx_training_exercise_add, name="hx-training-exercise-add"
    ),
    path(
        "<int:relation_id>/<int:training_id>/hx-training-exercise-delete",
        hx_views.hx_training_exercise_delete,
        name="hx-training-exercise-delete",
    ),
    path(
        "<int:relation_id>/<int:training_id>/hx-training-exercise-edit",
        hx_views.hx_training_exercise_edit,
        name="hx-training-exercise-edit",
    ),
]
