from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(Field("email", css_class="bg-dark"))
        self.helper.form_tag = False


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(Field("email", css_class="bg-dark"))
        self.helper.form_tag = False


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "birth_date", "avatar", "gender", "weight", "height"]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("first_name", css_class="bg-dark"),
            Field("last_name", css_class="bg-dark"),
            Field("birth_date", css_class="bg-dark"),
            Field("avatar", css_class="bg-dark"),
            Field("gender", css_class="bg-dark"),
            Field("weight", css_class="bg-dark"),
            Field("height", css_class="bg-dark"),
        )
        self.helper.form_tag = False
