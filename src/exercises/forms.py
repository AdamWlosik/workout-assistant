from django import forms

from exercises.models import Exercise


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = [
            "is_active",
            "name",
            "description",
            "category",
        ]
