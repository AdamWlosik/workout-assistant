from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from exercises.models import Exercise


class Category(models.Model):
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

    category = models.CharField(max_length=100, choices=CategoryChoices.choices, default="")

    def __str__(self):  # noqa: ANN204 # TODO (Adam) ruff poprawic
        return self.get_category_display()


class Training(models.Model):
    # class CategoryChoices(models.TextChoices):
    #     CHEST = "1", _("Chest")
    #     BACK = "2", _("Back")
    #     TRICEPS = "3", _("Triceps")
    #     FOREARM = "4", _("Forearm")
    #     LEGS = "5", _("Legs")
    #     SHOULDERS = "6", _("Shoulders")
    #     BICEPS = "7", _("Biceps")
    #     ABS = "8", _("ABS")
    #     GLUTES = "9", _("Glutes")
    #     NECKS = "10", _("Necks")
    #     WARM_UP = "11", _("Warm Up")
    #     CARDIO = "12", _("Cardio")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True)
    exercises = models.ManyToManyField(
        Exercise,
        through="TrainingExercise",
        verbose_name=_("Exercises"),
        related_name="trainings",
        default="",
        blank=True,
    )
    # TODO reps = ... ()kg x (), połączone z exercise czyli dodając excercise pojawia sie opcja dodania reps
    # category = models.CharField(max_length=100, choices=CategoryChoices)
    category = models.ManyToManyField(Category, verbose_name=_("Category"), default="", blank=True)
    # TODO categories = models.ManyToManyField() dalej nie działa puste okienko

    def __str__(self) -> str:
        return self.name


class TrainingExercise(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.CharField(max_length=50, blank=True, verbose_name=_("Reps (e.g., 10kg x 12)"))

    class Meta:
        unique_together = ("training", "exercise")

    def __str__(self):  # noqa: ANN204 # TODO (Adam) ruff poprawic
        return f"{self.training.name} - {self.exercise.name}"
