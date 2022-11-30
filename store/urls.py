from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.store),
    path("cart/", views.cart),
    path("checkout/", views.checkout),
]

























