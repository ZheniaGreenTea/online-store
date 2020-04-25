from django.urls import path
from .views import CategoryListView,CategoryDetailView

urlpatterns = [

#path('',views.first_function),
path('', CategoryListView.as_view(), name='category'),
path('category/<slug:slug>/',  CategoryDetailView.as_view(), name='detail_category'),
]