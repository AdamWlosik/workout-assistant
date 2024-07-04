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
            "categories",
            "exercises",
        ]
        widgets = {
            "categories": forms.CheckboxSelectMultiple(attrs={"class": "white-font"}),
            "exercises": forms.CheckboxSelectMultiple(attrs={"class": "white-font"}),
        }

    def __init__(self, *args, **kwargs) -> None:
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)
        self.fields["exercises"].queryset = Exercise.objects.filter(user=self.request.user)
        self.fields["categories"].queryset = Category.objects.all()

    def save(self, *, commit: bool = True) -> Training:
        # TODO FBT001 Boolean default positional argument in function definition
        # FBT002 Boolean default positional argument in function definition
        #  def save(self, *, commit: bool = True) -> Training:
        # globalny ignor w pyproject.toml
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()
        return instance
