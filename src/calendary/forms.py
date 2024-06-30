from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "date", "trainings"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "black-font"}),
        }

    def save(self, commit: bool = True) -> Event:
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()
        return instance
