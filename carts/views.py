from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import TemplateView
from carts.services import Cart
from products.models import Product
from django.contrib import messages
from django.views import View
# Create your views here.

class ToAddInSession(View):

    def get(self, request, slug):

        object = Product.objects.get(slug=slug)
        product_id = object.id
        product_id = str(product_id)
        quantity = request.GET['quan']
        quantity = int(quantity)
        css_rule = request.GET['st']
        add1 = request.GET['add1']

        if add1 == 'true':
            self.to_add(product_id, quantity)

        if 'css' not in request.session:
            request.session['css'] = {}
            request.session['css'] = css_rule
            request.session.save()
            return HttpResponse('')

        return HttpResponse('')

    def to_add(self,product_id,quantity):
        test = Cart(self.request)
        test.add(product_id,quantity)
        return HttpResponse('')


class ToCart(TemplateView):

    template_name = 'carts/cart.html'

    def get_context_data(self, *args, **kwargs):
                context = super(ToCart,
                                self).get_context_data(**kwargs)
                p_list = []
                price_all= []

                for key in self.request.session['cart']:

                    object = Product.objects.get(id=key)
                    name = object.name
                    id = object.id
                    quantity = self.request.session['cart'][key]
                    first_price = object.price
                    price = first_price * quantity
                    p_list.append([id,name,quantity,price,first_price ])
                    context['cart_list'] = p_list
                    price_all.append(price)

                    context['total_price']= sum(price_all)


                return context


class DelPlusMinusInCart(View):

    def get(self,request):

        product_id = request.GET['pk']
        btn = request.GET['btn']

        if btn == 'plus':

            quantity = request.GET['quan']
            quantity = int(quantity)
            self.to_add(product_id,quantity)

            return HttpResponse('')

        if btn == 'minus':

            quantity = request.GET['quan']
            quantity = int(quantity)
            self.minus(product_id,quantity)
            return HttpResponse('')

        if btn == 'delprod':

            self.remove(product_id)
            return HttpResponse('')


    def to_add(self, product_id, quantity):
        test = Cart(self.request)
        test.add(product_id, quantity)
        return HttpResponse('')

    def minus(self,product_id, quantity):
        test = Cart(self.request)
        test.minus(product_id,quantity)
        return HttpResponse('')

    def remove(self,product_id):
        test = Cart(self.request)
        test.remove(product_id)
        return HttpResponse('')



