from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _
from exercises.models import Exercise


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Training(models.Model):
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
    category = models.ManyToManyField(Category, verbose_name=_("Categories"), blank=True, related_name="trainings")

    def __str__(self) -> str:
        return self.name

    def get_category_display(self) -> str:
        return ", ".join(category.name for category in self.category.all())


class TrainingExercise(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    # reps = models.CharField(max_length=50, blank=True, verbose_name=_("Reps (e.g., 10kg x 12)"))
    # TODO ArrayFields
    reps = ArrayField(models.CharField(max_length=50, blank=True, verbose_name=_("Reps (e.g., '10kg x 12')")))

    def __str__(self) -> str:
        return f"{self.training.name} - {self.exercise.name}"
