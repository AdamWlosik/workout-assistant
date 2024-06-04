from django.urls import path

from . import views

urlpatterns = [
    path("", views.trainings_list, name="trainings"),
    path("<int:training_id>/", views.training_detail, name="training_detail"),
    path("create/", views.training_create, name="training_create"),
    path("<int:training_id>/edit/", views.training_edit, name="training_edit"),
    path("<int:training_id>/delete/", views.training_delete, name="training_delete"),
]
