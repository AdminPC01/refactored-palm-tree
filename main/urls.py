from django.urls import path
from . import views
urlpatterns = [
    path("view/", views.view),
    path("v2/<str:pk>/", views.v2),
]