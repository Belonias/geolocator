# new in django 1.11
from django.contrib.auth.views import LogoutView as DefaultLogoutView, LoginView as DefaultLoginView
from django.shortcuts import render
from analytics.signals import user_logged_in

# Create your views here.
from .forms import LoginForm

class LoginView(DefaultLoginView):
    authentication_form = LoginForm

    def form_valid(self, form):
        # overidin the formview
        # nothing to do with the login view
        done_ = super(LoginView, self).form_valid(form)
        if self.request.user.is_authenticated():
            # use signal
            user_logged_in.send(self.request.user, request=self.request)
        return done_


class LogoutView(DefaultLogoutView):
    pass
