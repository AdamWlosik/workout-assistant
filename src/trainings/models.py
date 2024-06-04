from typing import TYPE_CHECKING

from django.conf import settings
from django.db import models

if TYPE_CHECKING:
    from django.forms import CharField

# TODO TCH004 Move import `django.forms.CharField` out of type-checking block.
#  Import is used for more than type hinting.


class Trainings(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # noqa: DJ001
    # TODO Avoid using `null=True` on string-based fields such as `TextField` tak?
    exercises = models.TextField(blank=True, null=True)  # noqa: DJ001
    category = models.CharField(
        max_length=100,
        choices=[
            ("Chest", "Chest"),
            ("Back", "Back"),
            ("Triceps", "Triceps"),
            ("Forearm", "Forearm"),
            ("Legs", "Legs"),
            ("Shoulders", "Shoulders"),
            ("Biceps", "Biceps"),
            ("ABS", "ABS"),
            ("Glutes", "Glutes"),
            ("Neck", "Neck"),
            ("Warm-Up", "Warm-Up"),
            ("Cardio", "Cardio"),
        ],
    )

    def __str__(self) -> CharField:
        return self.name
