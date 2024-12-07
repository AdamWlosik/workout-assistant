from django import forms

from trainings.models import Training
from .models import Event


class EventForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["trainings"].queryset = Training.objects.filter(user=user)

    class Meta:
        model = Event
        fields = ["title", "description", "date", "trainings"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "black-font"}),
        }

    def save(self, *, commit: bool = True) -> Event:
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()
        return instance
