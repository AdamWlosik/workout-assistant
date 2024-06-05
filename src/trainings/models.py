# from typing import TYPE_CHECKING

from django.conf import settings
from django.db import models

# if TYPE_CHECKING:
#     from django.forms import CharField


class Training(models.Model):
    category_choices = {
        "Chest": "Chest",
        "Back": "Back",
        "Triceps": "Triceps",
        "Forearm": "Forearm",
        "Legs": "Legs",
        "Shoulders": "Shoulders",
        "Biceps": "Biceps",
        "ABS": "ABS",
        "Glutes": "Glutes",
        "Neck": "Neck",
        "Warm-Up": "Warm-Up",
        "Cardio": "Cardio",
    }
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True)
    exercises = models.TextField(default="", blank=True)
    category = models.CharField(max_length=100, choices=category_choices)

    def __str__(self) -> str:  # TODO ma być str czy CharField
        return self.name
