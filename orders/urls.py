import self as self
from django.contrib.auth.views import LogoutView

from . import views
from django.urls import path

from .views import OrderPageView,CopyProduct

urlpatterns = [
    path('to_show_orders/', OrderPageView.as_view(), name='orders_page'),
    path('ordering/', views.artifical_post),
    path('orders/', CopyProduct.as_view()),

]