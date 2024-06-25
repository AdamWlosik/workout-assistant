from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "date", "trainings"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "black-font"}),
        }

    def save(self, commit=True):  # noqa: ANN201 FBT002 ANN001 #TODO (Adam) ruff poprawic
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()
        return instance
