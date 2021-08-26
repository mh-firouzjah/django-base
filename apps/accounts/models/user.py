from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    def get_full_name(self):
        return (self.first_name + self.last_name) or self.username

    def __str__(self):
        return self.get_full_name()