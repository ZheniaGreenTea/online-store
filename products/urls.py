from django.urls import path
from .views import ProductListView, ProductDetailView,ProductInSession

urlpatterns = [

    # path('',views.first_function),
    path('', ProductListView.as_view(), name='general_page'),
    path('category/<slug:slug>/', ProductListView.as_view(), name='products'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('<slug:slug>/quantity/', ProductInSession.as_view(), name='inside_cart')
]
