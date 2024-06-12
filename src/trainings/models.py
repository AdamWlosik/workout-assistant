from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Training(models.Model):
    class CategoryChoices(models.TextChoices):
        CHEST = "1", _("Chest")
        BACK = "2", _("Back")
        TRICEPS = "3", _("Triceps")
        FOREARM = "4", _("Forearm")
        LEGS = "5", _("Legs")
        SHOULDERS = "6", _("Shoulders")
        BICEPS = "7", _("Biceps")
        ABS = "8", _("ABS")
        GLUTES = "9", _("Glutes")
        NECKS = "10", _("Necks")
        WARM_UP = "11", _("Warm Up")
        CARDIO = "12", _("Cardio")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True)
    exercises = models.TextField(default="", blank=True)
    category = models.CharField(max_length=100, choices=CategoryChoices)

    def __str__(self) -> str:
        return self.name
