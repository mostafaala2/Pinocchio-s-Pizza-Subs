from django.urls import path

from . import views

urlpatterns = [
    path("", views.manus, name="manus"),
    path('cart/', views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
]
