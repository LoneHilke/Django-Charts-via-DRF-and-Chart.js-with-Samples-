from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from apps.models import BaseModel

# Create your models here.

class User(AbstractUser, BaseModel):
    has_purchased = models.BooleanField(default=False)

