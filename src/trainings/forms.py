from crispy_forms.bootstrap import InlineCheckboxes
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div
from django import forms
from django.forms import inlineformset_factory
from django_jsonform.forms.fields import ArrayFormField

from trainings.models import Category, Training, TrainingExercise


class TrainingExerciseForm(forms.ModelForm):
    reps = ArrayFormField(forms.CharField)  # TODO Bartek sprawdź

    class Meta:
        model = TrainingExercise
        fields = ["exercise", "reps"]
        widgets = {
            # "reps": forms.TextInput(attrs={"placeholder": "e.g., 10kg x 12"}),
            # my_field = JSONFormField(schema=schema)
            # "reps": JSONFormField(schema=schema)
            "exercise": forms.Select(attrs={"class": "form-control"}),
            # TODO wyswietla exercise wszystkich użytkowników, nie działa Save w edit_training,
        }

        def __init__(self, *args, **kwargs) -> None:
            self.request = kwargs.pop("request")
            super().__init__(*args, **kwargs)


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = [
            "is_active",
            "name",
            "description",
            "category",
        ]
        widgets = {
            "category": forms.CheckboxSelectMultiple(attrs={"class": "white-font"}),
        }

    def __init__(self, *args, **kwargs) -> None:
        self.request = kwargs.pop("request")
        self.formset_data = kwargs.pop("formset_data", None)
        super().__init__(*args, **kwargs)
        self.fields["category"].queryset = Category.objects.all()
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("is_active"),
            Div(
                Field("name", css_class="bg-dark"),
                css_class="col-md-6",
            ),
            Field("description", css_class="bg-dark"),
            InlineCheckboxes("category"),
            # TODO ustawić rowno
        )


TrainingExerciseFormSet = inlineformset_factory(
    Training, TrainingExercise, form=TrainingExerciseForm, extra=1, can_delete=True, can_order=True
)
