from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Exercise(models.Model):
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
        CORE = "13", _("Core")
        OTHER = "14", _("Other")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    description = models.TextField(default="", blank=True)
    category = models.CharField(max_length=100, choices=CategoryChoices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["created_at"]
