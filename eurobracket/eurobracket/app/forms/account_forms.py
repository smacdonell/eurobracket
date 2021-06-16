from django import forms
from .base_form import BaseForm


class LoginForm(BaseForm):
    username = forms.CharField(label='Username', max_length=32, required=True)
    password = forms.CharField(label='Password', max_length=32, required=True)

    def clean(self):
        cd = super().clean()


class CreateAccountForm(BaseForm):
    username = forms.CharField(label='Username', max_length=32, required=True)
    password = forms.CharField(label='Password', max_length=32, min_length=8, required=True)
    confirm_password = forms.CharField(label='Confirm Password', max_length=32, min_length=8, required=True)
    first_name = forms.CharField(label='First Name', max_length=32, required=True)
    last_name = forms.CharField(label='Last Name', max_length=32, required=True)

    def clean_confirm_password(self):
        cd = self.cleaned_data
        breakpoint()

    def clean(self):
        cd = super().clean()
