from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jsonform.models.fields import ArrayField
from exercises.models import Exercise


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Training(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_copy = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True)
    # TODO tutaj sortowanie
    exercises = models.ManyToManyField(
        Exercise,
        through="TrainingExercise",
        verbose_name=_("Exercises"),
        related_name="trainings",
        default="",
        blank=True,
    )
    category = models.ManyToManyField(Category, verbose_name=_("Categories"), blank=True, related_name="trainings")

    def __str__(self) -> str:
        return self.name

    def get_category_display(self) -> str:
        return ", ".join(category.name for category in self.category.all())


class TrainingExercise(models.Model):
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = ArrayField(models.CharField(max_length=50, blank=True, verbose_name=_("Reps (e.g., '10kg x 12')")))
    reps_proposed = ArrayField(models.CharField(max_length=50, blank=True, verbose_name=_("Reps (e.g., '10kg x 12')")))
    history = models.TextField(default="[]", blank=True)

    def __str__(self) -> str:
        return f"{self.training.name} - {self.exercise.name}"

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
