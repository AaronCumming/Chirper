import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class DeckQuerySet(models.QuerySet["Chirp"]):
        
    def all_parent_chirps(self):
        return self.filter(parent_chirp_id__isnull=True)
    
    
    def all_children_on_parent_chirp(self, chirp_id):
        return self.filter(paren_chirp_id = chirp_id)
      

class Chirp(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    chirp_name = models.CharField(max_length=255)
    time_created = models.DateTimeField("date published", default=timezone.now)
    chirp_body = models.TextField()
    parent_chirp_id = models.ForeignKey("chirper.Chirp", on_delete=models.CASCADE, null=True, blank=True, related_name="replies", default=None)

    objects: DeckQuerySet = DeckQuerySet.as_manager()

    def __str__(self):
        return self.chirp_name
    
    def was_published_recently(self):
        return self.time_created >= timezone.now() - datetime.timedelta(days=1)

        
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chirp = models.ForeignKey(Chirp, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'chirp')
