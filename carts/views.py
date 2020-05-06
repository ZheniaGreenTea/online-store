from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product
from django.contrib import messages
from django.views import View
# Create your views here.

class ProductInSession(View):

    def get(self, request,slug):
        object = Product.objects.get(slug=slug)
        quantity = request.GET['prod']

        if 'cart' not in request.session:
            request.session['cart'] = {}
            request.session['cart']['product_id'] = object.id
            request.session['cart']['quantity'] = quantity
            request.session.modified = True
            print('*session cart* если нет {}',request.session['cart'])
            messages.info(request, 'товар добавлен в корзину!')
            return render(request, 'carts/cart.html')

        else:
            request.session['cart']['product_id'] = object.id
            request.session['cart']['quantity'] = quantity
            request.session.modified = True
            print('*session cart 2 * если есть {} ', request.session['cart'])
            messages.info(request, 'товар добавлен в корзину')
            return render(request, 'carts/cart.html')