"""
models.py
Aaron Cumming
2025-02-25
"""

import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChirpQuerySet(models.QuerySet["Chirp"]):
    """Custom Query Set for the Chirp model."""

    def all_parent_chirps(self):
        """Provides all parent chirps in database."""
        return self.filter(parent_chirp_id__isnull=True)
    
    def all_children_on_parent_chirp(self, chirp_id):
        """Provides all replies to a parent chirp, given a parent chirp."""
        return self.filter(paren_chirp_id = chirp_id)
      

class Chirp(models.Model):
    """ Includes parent chirps and replies.
        Parent chirps have parent_chirp_id equal to null.
        Deleted users' chirps have the user equal to null.
    """

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    chirp_name = models.CharField(max_length=255)
    time_created = models.DateTimeField("date published", default=timezone.now)
    chirp_body = models.TextField()
    parent_chirp_id = models.ForeignKey("chirper.Chirp", on_delete=models.CASCADE, null=True, blank=True, related_name="replies", default=None)

    objects: ChirpQuerySet = ChirpQuerySet.as_manager()

    def __str__(self):
        return self.chirp_name
    
        
class Like(models.Model):
    """ A chirp can have multiple likes.
        A user can like multiple chirps.
        A certain user can only like a certain chirp once.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chirp = models.ForeignKey(Chirp, on_delete=models.CASCADE)


    class Meta:
        """Ensures that a certain user can only like a certain chirp once."""
        unique_together = ('user', 'chirp')
