from django.urls import path
from . import views
urlpatterns = [
    path("", views.main, name="main"),
    path("single-project/<str:pk>/", views.project, name="project"),
    path("create/", views.create, name="create"),
    path("delete/<str:pk>/", views.delete, name="delete"),
    path("update_project/<str:pk>/", views.update_project, name="update_project"),
]