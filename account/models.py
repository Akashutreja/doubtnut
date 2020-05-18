from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime

class UserProfile(models.Model):
  email = models.EmailField(blank=False)
  questions = ArrayField(
            models.CharField(max_length=10, blank=True),
            size=8,
        )
  last_activity = models.DateTimeField(default=datetime.datetime.now, blank=True)
  email_sent = models.BooleanField(default=False)