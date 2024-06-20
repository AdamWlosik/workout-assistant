from django.urls import path

from calendary import views

urlpatterns = [
    path("", views.calendar_view, name="calendary_view"),
    path("add-event", views.add_event, name="add_event"),
    path("<int:event_id>/", views.event_detail, name="event_detail"),
    path("<int:event_id>/edit/", views.event_edit, name="event_edit"),
]
