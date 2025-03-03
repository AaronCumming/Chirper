import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Chirp(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    chirp_name = models.CharField(max_length=255)
    time_created = models.DateTimeField("date published")
    chirp_body = models.TextField()
    parent_chirp_id = models.ForeignKey("chirper.Chirp", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.chirp_name
    
    def was_published_recently(self):
        return self.time_created >= timezone.now() - datetime.timedelta(days=1)

        