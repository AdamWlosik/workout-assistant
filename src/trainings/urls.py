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
    path(
        "<int:event_id>/<int:relation_id>/<int:training_id>/rep/<int:rep_index>/",
        hx_views.hx_training_exercise_rep_edit,
        name="hx-training-exercise-rep-edit",
    ),
    path(
        "hx-training-exercise-rep-add/<int:relation_id>/<int:training_id>/",
        hx_views.hx_training_exercise_rep_add,
        name="hx-training-exercise-rep-add"),
    # path(
    #     "mark-done-exercise/<int:training_exercise_id>/<int:event_id>/",
    #     views.mark_done_exercise,
    #     name="mark-done-exercise"),
    path(
        "display-history/<int:training_exercise_id>/<int:event_id>/",
        views.display_history,
        name="display-history"),
]
