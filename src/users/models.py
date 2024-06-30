from __future__ import annotations

from typing import TYPE_CHECKING

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

if TYPE_CHECKING:
    from django.forms import EmailField


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> EmailField:
        return self.email


class Profile(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = "M", _("Male")
        FEMALE = "F", _("Female")

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=False, default="", blank=True)
    last_name = models.CharField(max_length=30, null=False, default="", blank=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GenderChoices, null=False, default="", blank=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user.email} Profile"

    @property
    def bmi(self) -> float | None:
        """Method for calculating BMI"""
        if self.weight and self.height:
            return self.weight / (self.height / 100) ** 2
        return None


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender: type[CustomUser], instance: CustomUser, created: bool, **kwargs: dict) -> None:
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender: type[CustomUser], instance: CustomUser, **kwargs: dict) -> None:
    if hasattr(instance, "profile_view"):
        instance.profile.save()
