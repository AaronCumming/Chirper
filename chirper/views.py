from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

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
    

class CreateChirpView(generic.CreateView):
    model = Chirp
    fields = ["chirp_name", "chirp_body"]
    template_name = "chirper/chat/chirp_create.html"
    success_url = reverse_lazy("chirper:home")


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


    #form_class = GameForm
    """
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs
    """