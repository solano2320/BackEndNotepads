from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    email = models.EmailField(blank=False, unique=True)
    birth_date = models.DateField(null=True, blank=True)
