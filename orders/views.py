from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

from orders.forms import OrderForm
from products.models import Product
from orders.models import NovayaPochta, UkrPochta, OrderProduct, Status

from django.views.generic.base import TemplateView



class OrderPageView(TemplateView):

    template_name = "orders/order.html"

    def get_context_data(self, **kwargs):
        print('OrderPageView ')
        context = super().get_context_data(**kwargs)
        order_list = []
        price_all = []
        user_cart = self.request.session['cart']
        global total_order_price

        for key in user_cart:
            object = Product.objects.get(id=key)
            name = object.name
            quantity = self.request.session['cart'][key]
            first_price = object.price
            price = first_price * quantity
            price_all.append(price)

            order_list.append([name, quantity, price])
            total_order_price = sum(price_all)

        order_f = OrderForm()
        context['order_form']= order_f
        context['order_list']= order_list
        context['total_price']= total_order_price
        return context



class CopyProduct(View):


    def get(self, request, *args, **kwargs):
        print('CopyProduct ',request)
        user_cart = request.session['cart']
        for key in user_cart:
            object = Product.objects.get(id=key)
            copy_product = object
            for name in copy_product.author.all():

               copy_orderproduct = OrderProduct(name=copy_product.name, author=name, description=copy_product.description,
                                     price=copy_product.price, product_id=copy_product.id)
               copy_orderproduct.save()
        return redirect('orders_page')


def artifical_post(request):
    """ функция ведет на обработку формы """

    order_f = OrderForm(request.POST)
    id_status = request.POST['payment_method']
    id_status = int(id_status)
    s = Status.objects.get(id=id_status)
    new_status = order_f.save(commit=False)
    new_status.current_status = s
    new_status.save()
    return redirect('orders_page')

