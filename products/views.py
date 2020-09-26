from django.shortcuts import render
from django.views.generic import ListView, DetailView
#from django.shortcuts import get_object_or_404, render
from django.views import View
from django.shortcuts import redirect
from .models import Category,Product


class ProductListView(ListView):
    """вывод списка категорий и списка товаров"""

    model = Category
    template_name = 'products/base.html'


    def get_context_data(self, *args, **kwargs):

                context = super(ProductListView,
                                self).get_context_data(**kwargs)
                category_slug = self.kwargs.get('slug')
                if category_slug:
                    category = Category.objects.get(slug=category_slug)
                    context['products'] = category.product_set.all()
                    return context

                return context




class ProductDetailView(DetailView):
    """вывод полного описания товара"""
    model = Product
    template_name = 'products/product_detail.html'
    slug_url_kwarg = 'slug'


    def get_context_data(self, *args, **kwargs):
        """если юзер еще не добавлял товар - кнопка корзина скрыта"""
        context = super(ProductDetailView,
                        self).get_context_data(**kwargs)

        if 'css' not in self.request.session:
                return context
        else:
            visible = self.request.session['css']

            if visible != " ":
                context['vis'] = visible
                return context




























        





