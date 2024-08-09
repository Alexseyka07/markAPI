from django.urls import path
from . import views

urlpatterns = [
    path("model", views.models, name="models"),
    path("mark", views.marks, name="marks"),
    path("part", views.parts, name="parts")
]