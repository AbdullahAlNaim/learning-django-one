from django.urls import path

from . import views

app_name = "poll"
urlpatterns = [
  path("", views.IndexView.as_view(), name="index"),
  path("<int:pk>/", views.DetailView.as_view(), name="detail"),
  path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
  path("<int:question_id>/vote/", views.vote, name="vote"),
]

# my dir
# C:\Users\aanai\Desktop\Developer\python\django_one\mysite\poll\templates\polls
# app search
# C:\Users\aanai\Desktop\Developer\python\django_one\mysite\poll\templates\poll\detail.html 