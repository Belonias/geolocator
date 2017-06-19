from django.conf import settings
from django.db import models

from .signals import user_logged_in
from .utils import get_client_city_data, get_client_ip

# Create your models here.
class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    session_key = models.CharField(max_length=60, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    city_data = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=120, null=True, blank=True)
    country = models.CharField(max_length=120, null=True, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.city_data:
            return str(self.city_data)
        else:
            return self.user.username

def user_logged_in_receiver(sender, request, *args, **kwargs):
    user = sender
    city_data = None
    ip_address = get_client_ip(request)
    if ip_address:
        city_data = get_client_city_data(ip_address)
    session = request.session.session_key
    UserSession.objects.create(
        user=user,
        session_key=session,
        ip_address=ip_address,
        city_data=city_data,)
    #request # we need to parse this to get the IP Address
    #UserSession.objects.create()

# we make the receiver connection
user_logged_in.connect(user_logged_in_receiver)
