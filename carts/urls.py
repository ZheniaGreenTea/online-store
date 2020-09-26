from django.contrib.auth.views import LogoutView

from .views import ToAddInSession, ToCart,DelPlusMinusInCart
from . import views
from django.urls import path

urlpatterns = [
path('<slug:slug>/quantity/', ToAddInSession.as_view(), name='inside_sesson'),
path('tocart/', ToCart.as_view(), name='inside_cart'),
path('dpm/',DelPlusMinusInCart.as_view()),
]