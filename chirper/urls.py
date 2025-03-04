from django.urls import path

from . import views

app_name = "chirper"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
]