from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from trainings.models import Training


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    trainings = models.ManyToManyField(Training, verbose_name=_("Training"), blank=True, related_name="events")

    def __str__(self) -> str:
        return self.title
