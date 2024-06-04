from django import forms

from trainings.models import Trainings


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Trainings
        fields = [
            "is_active",
            "name",
            "description",
            "exercises",
            "category",
        ]
