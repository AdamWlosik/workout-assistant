from django.urls import path

from dashboard import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
]
