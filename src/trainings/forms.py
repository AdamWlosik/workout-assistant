from django import forms
from exercises.models import Exercise

from trainings.models import Category, Training


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = [
            "is_active",
            "name",
            "description",
            "category",
            "exercises",
        ]
        widgets = {
            "category": forms.CheckboxSelectMultiple(attrs={"class": "white-font"}),
            "exercises": forms.CheckboxSelectMultiple(attrs={"class": "white-font"}),
        }

    def __init__(self, *args, **kwargs):  # noqa: ANN204 #TODO (Adam) ruff poprawic
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)
        self.fields["exercises"].queryset = Exercise.objects.filter(user=self.request.user)
        self.fields["category"].queryset = Category.objects.all()

    def save(self, commit=True):  # noqa: ANN201 FBT002 ANN001 #TODO (Adam) ruff poprawic
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()
        return instance
