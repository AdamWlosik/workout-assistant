from django import forms
from django.forms import inlineformset_factory

from trainings.models import Category, Training, TrainingExercise


class TrainingExerciseForm(forms.ModelForm):
    class Meta:
        model = TrainingExercise
        fields = ["exercise", "reps"]
        widgets = {
            "reps": forms.TextInput(attrs={"placeholder": "e.g., 10kg x 12"}),
            "exercise": forms.Select(attrs={"class": "form-control"}),
            # TODO wyswietla exercise wszystkich użytkowników, nie działa Save w edit_training,
            #  nie działa Remove i Add Excercise
        }


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = [
            "is_active",
            "name",
            "description",
            "category",
            # "exercises",
        ]
        widgets = {
            "category": forms.CheckboxSelectMultiple(attrs={"class": "white-font"}),
        }

    def __init__(self, *args, **kwargs) -> None:
        self.request = kwargs.pop("request")
        self.formset_data = kwargs.pop("formset_data", None)
        super().__init__(*args, **kwargs)
        self.fields["category"].queryset = Category.objects.all()
        # self.fields["exercises"].queryset = Exercise.objects.filter(user=self.request.user)

        if self.instance.pk:
            self.formset = TrainingExerciseFormSet(
                data=self.formset_data,
                instance=self.instance,
                queryset=TrainingExercise.objects.filter(training=self.instance),
            )
        else:
            self.formset = TrainingExerciseFormSet(
                data=self.formset_data, instance=self.instance, queryset=TrainingExercise.objects.none()
            )

    def is_valid(self):  # noqa: ANN201 # TODO Missing return type annotation for public function `is_valid`
        return super().is_valid() and self.formset.is_valid()

    def save(self, commit: bool = True):  # noqa: ANN201 FBT002 FBT001
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()
            training_exercises = self.formset.save(commit=False)
            for training_exercise in training_exercises:
                training_exercise.training = instance
                training_exercise.save()
            self.formset.save_m2m()
        return instance


TrainingExerciseFormSet = inlineformset_factory(
    Training, TrainingExercise, form=TrainingExerciseForm, extra=1, can_delete=True, can_order=True
)
