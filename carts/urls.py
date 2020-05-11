from django.contrib.auth.views import LogoutView

from .views import ProductInSession, ToCart
from . import views
from django.urls import path

urlpatterns = [
path('<slug:slug>/quantity/', ProductInSession.as_view(), name='inside_sesson'),
path('to_cart/', ToCart.as_view(),name='inside_cart'),
]