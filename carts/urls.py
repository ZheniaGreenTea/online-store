from django.contrib.auth.views import LogoutView

from .views import ProductInSession
from . import views
from django.urls import path

urlpatterns = [
path('<slug:slug>/quantity/', ProductInSession.as_view(), name='inside_cart'),

]