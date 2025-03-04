from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Chirp

# Create your views here.
class HomeView(generic.ListView):
    template_name = "chirper/chat/home.html"
    context_object_name = "parent_chirper_list"

    def get_queryset(self):
        """Return all of the Chirps."""
        return Chirp.objects.order_by("-time_created").all_parent_chirps().prefetch_related("replies")
    

class DetailView(generic.DetailView):
    model = Chirp
    template_name = "chirper/chat/chirp_detail.html"

    def get_queryset(self):
        """Return all of the Chirps."""
        return Chirp.objects.order_by("-time_created").all_parent_chirps().prefetch_related("replies")