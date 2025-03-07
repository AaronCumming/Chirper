"""
views.py
Aaron Cumming
2025-02-25
"""

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth import logout

from .models import Chirp, User


# Create your views here.
class HomeView(generic.ListView):
    """Displays the home page and all chirps and replies."""
    template_name = "chirper/chat/home.html"
    context_object_name = "parent_chirper_list"

    def get_queryset(self):
        """Return all of the Chirps."""
        return Chirp.objects.order_by("-time_created").all_parent_chirps().prefetch_related("replies")
    

class DetailView(generic.DetailView):
    """Displays a certain parent chirp and all replies."""
    model = Chirp
    template_name = "chirper/chat/chirp_detail.html"

    def get_queryset(self):
        """Return all of the Chirps."""
        return Chirp.objects.order_by("-time_created").all_parent_chirps().prefetch_related("replies")
    

class ProfileView(generic.DetailView):
    """Displays profile for logged in user and allows the user to delete account and/or chirps."""
    model = User
    template_name = "chirper/chat/profile.html"

    def post(self, request, *args, **kwargs):
        """User can choose to delete account with or without deleting chirps."""
        user = request.user
        action = request.POST.get("delete_action")

        if action == "keep_chirps":
            Chirp.objects.filter(user=user).update(user=None)
            user.save()

        elif action == "delete_all":
            Chirp.objects.filter(user=user).delete()
            user.delete()

        logout(request)
        return redirect(reverse_lazy("chirper:home"))      


class CreateChirpView(generic.CreateView):
    """User can create a parent chirp."""
    model = Chirp
    fields = ["chirp_name", "chirp_body"]
    template_name = "chirper/chat/chirp_create.html"
    success_url = reverse_lazy("chirper:home")

    def form_valid(self, form):
        """Fills in the user id for the current user behind the scenes."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class CreateReplyView(generic.CreateView):
    """User can reply to a parent chirp."""
    model = Chirp
    fields = ["chirp_name", "chirp_body"]
    template_name = "chirper/chat/chirp_create_reply.html"

    def get_context_data(self, **kwargs):
        """Adds parent chirp id to the template."""
        context = super().get_context_data(**kwargs)
        context["parent_chirp"] = get_object_or_404(Chirp, id=self.kwargs["parent_id"])
        return context

    def form_valid(self, form):
        """Fills in the parent chirp id and user id  for the current user behind the scenes."""
        form.instance.user = self.request.user
        parent_id = self.kwargs.get("parent_id")
        form.instance.parent_chirp_id = get_object_or_404(Chirp, id=parent_id)
        return super().form_valid(form)

    def get_success_url(self):
        """Goes back to parent chirp page after replying."""
        return reverse_lazy("chirper:detail", kwargs={"pk":self.kwargs["parent_id"]})