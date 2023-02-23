from django.urls import path
from . import views
urlpatterns = [
    path("main/", views.main, name="main"),
    path("single-project/<str:pk>/", views.project, name="project"),
    path("create/", views.create, name="create"),
]