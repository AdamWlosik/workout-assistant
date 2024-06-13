from django import forms
from django.forms import modelformset_factory
from exercises.models import Exercise

from trainings.models import Category, Training, TrainingExercise


class TrainingExerciseForm(forms.ModelForm):
    class Meta:
        model = TrainingExercise
        fields = ["exercise", "reps"]
        widgets = {
            "reps": forms.TextInput(attrs={"placeholder": "e.g., 10kg x 12"}),
            "exercise": forms.Select(attrs={"class": "form-control"}),
        }


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

        self.TrainingExerciseFormSet = modelformset_factory(TrainingExercise, form=TrainingExerciseForm, extra=1)
        self.formset = self.TrainingExerciseFormSet(queryset=TrainingExercise.objects.none())

    def is_valid(self):  # noqa: ANN201 #TODO (Adam) ruff poprawic
        return super().is_valid() and self.formset.is_valid()

    def save(self, commit=True):  # noqa: ANN201 FBT002 ANN001 #TODO (Adam) ruff poprawic
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()
            self.formset.save(commit=False)
            for form in self.formset:
                if form.cleaned_data:
                    training_exercise = form.save(commit=False)
                    training_exercise.training = instance
                    training_exercise.save()
        return instance
