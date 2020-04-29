from django.urls import path
from .views import ProductListView

urlpatterns = [

    # path('',views.first_function),
    path('', ProductListView.as_view(), name='general_page'),
    path('category/<slug:slug>/', ProductListView.as_view(), name='products'),
]
