from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Product
from django.contrib import messages
from django.views import View
# Create your views here.

class ProductInSession(View):

    def get(self, request,slug):
        object = Product.objects.get(slug=slug)
        quantity = request.GET['prod']
        css_rule = request.GET['st']

        if 'css' not in request.session:
            request.session['css'] = {}
            request.session['css']['style'] = css_rule
            request.session.modified = True

        if 'cart' not in request.session:
            request.session['cart'] = {}
            request.session['cart']['product_id']= object.id
            request.session['cart']['quantity']= quantity
            request.session.modified = True
            return HttpResponse(" ")

        else:
            request.session['cart']['product_id'] = object.id
            request.session['cart']['quantity'] = quantity
            request.session.modified = True
            return HttpResponse(" ")


class ToCart(TemplateView):

    template_name = 'carts/cart.html'

    def get_context_data(self, *args, **kwargs):

                context = super(ToCart,
                                self).get_context_data(**kwargs)
                product_id = self.request.session['cart']['product_id']
                quantity = self.request.session['cart']['quantity']
                current_product = Product.objects.get(id=product_id)
                price = current_product.price
                context['product']=current_product
                context['quantity'] = quantity
                context['price'] = price

                return context





