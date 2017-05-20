# new in django 1.11
from django.contrib.auth.views import LoginView as DefaultLoginView
from django.shortcuts import render

# Create your views here.
from .forms import LoginForm

class LoginView(DefaultLoginView):
    authentication_form = LoginForm
