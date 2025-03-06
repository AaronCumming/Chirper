from django.urls import path

from . import views

app_name = "chirper"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("profile/<int:pk>", views.ProfileView.as_view(), name="profile"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("create/", views.CreateChirpView.as_view(), name="create"),
    path("<int:parent_id>/create/", views.CreateReplyView.as_view(), name="create_reply"),
]