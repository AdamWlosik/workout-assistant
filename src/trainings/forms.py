from django import forms

from trainings.models import Training


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = [
            "is_active",
            "name",
            "description",
            "exercises",
            "category",
        ]
