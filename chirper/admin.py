from django.contrib import admin

# Register your models here.
from .models import Chirp, Like

admin.site.register(Chirp)
admin.site.register(Like)
