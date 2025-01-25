from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Layout
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("is_active"),
            Div(
                Field("name", css_class="bg-dark"),
                css_class="col-md-6",
            ),
            Field("description", css_class="bg-dark"),
            Field("category", css_class="bg-dark"),
        )
        self.helper.form_tag = False
