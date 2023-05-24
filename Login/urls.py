from django.urls import path

from . import views

urlpatterns = [
    path("", views.Login, name = "Login"),
    path("Fotitos", views.Fotitos, name = "Fotitos"),
    path("Dibujos", views.Dibujos, name = "Dibujos"),
]
