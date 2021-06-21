from django import forms
from django.contrib.auth import password_validation, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from eurobracket.app.forms.base_form import BaseForm


class LoginForm(BaseForm):
    error_messages = {
        'not_valid': 'The login information you provided is not valid.',
    }

    username = forms.CharField(label='Username', max_length=32, required=True)
    password = forms.CharField(label='Password', max_length=32, required=True)

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise ValidationError(
                    self.error_messages['not_valid'],
                    code='not_valid'
                )

    def clean(self):
        cd = super().clean()


class CreateAccountForm(BaseForm):
    error_messages = {
        'username_taken': 'There is already an account with that username.',
        'email_taken': 'There is already an account with that email address.',
        'password_mismatch': 'The two password fields didn’t match.',
    }

    username = forms.CharField(label='Username', max_length=32, required=True)
    password = forms.CharField(label='Password', max_length=32, min_length=8, required=True)
    confirm_password = forms.CharField(label='Confirm Password', max_length=32, min_length=8, required=True)
    first_name = forms.CharField(label='First Name', max_length=32, required=True)
    last_name = forms.CharField(label='Last Name', max_length=32, required=True)
    email = forms.CharField(label='Email', max_length=64, required=True)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            exists = User.objects.filter(username=username)
            if exists:
                raise ValidationError(
                    self.error_messages['username_taken'],
                    code='username_taken'
                )
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            exists = User.objects.filter(email=email)
            if exists:
                raise ValidationError(
                    self.error_messages['email_taken'],
                    code='email_taken'
                )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return confirm_password

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get('confirm_password')
        if password:
            try:
                password_validation.validate_password(password)
            except ValidationError as error:
                self.add_error('confirm_password', error)

    def clean(self):
        cd = super().clean()
