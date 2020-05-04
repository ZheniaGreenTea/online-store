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



class ProductInSession(View):

    def get(self, request, slug):
        object = Product.objects.get(slug=slug)
        quantity = request.GET['prod']

        if 'cart' not in request.session:
            request.session['cart'] = {}
            request.session['cart']['product_id'] = object.id
            request.session['cart']['quantity'] = quantity
            request.session.modified = True
            print('******session cart*******',request.session['cart'])
            return render(request,'carts/cart.html')

        else:
            del request.session["cart"]
            print('session- - -', request.session)
            return render(request, 'products/product_detail.html')




















        





