from django import forms
# new in django 1.11
from django.contrib.auth.forms import AuthenticationForm
#from analytics import models


class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError('This account is inactive', code='inactive')
