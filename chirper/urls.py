from django.urls import path

from . import views

app_name = "chirper"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("create/", views.CreateChirpView.as_view(), name="create"),
    path("create_reply/", views.CreateReplyView.as_view(), name="create_reply"),
]