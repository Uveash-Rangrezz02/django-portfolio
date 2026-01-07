from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),   # ✅ HOME ROUTE
    path("contact/", views.contact, name="contact"),
]
