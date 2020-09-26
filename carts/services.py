from django.conf import settings
from django.http import HttpResponse

from products.models import Product


class Cart():
    """Инициализация объекта корзины."""
    def __init__(self, request):
        self.session = request.session

    def add(self,product_id,quantity):

        print('something is working', product_id,quantity)

        if 'cart' not in self.session:
            self.session['cart'] = {}
            self.session['cart'] = {product_id: quantity}
            self.session.save()
            print('добавилось в пустую корзину:',self.session['cart'])

        elif product_id not in self.session['cart']:
            self.session['cart'][product_id] = quantity
            print('нет дублей', self.session['cart'])
            self.session.save()

        else:
            print('request.session[cart] DO изменений', self.session['cart'])
            current_quantity = self.session['cart'][product_id]
            print('current_quantity:',current_quantity)
            new_quantity = current_quantity + 1
            print('new_quantity::',new_quantity)
            self.session['cart'][product_id] = new_quantity
            self.session.save()
            print('request.session[cart] после изменений', self.session['cart'])


    def minus(self,product_id,quantity):

            print('minus DO изменений:', self.session['cart'],'quantity arg:',quantity )
            current_quantity = self.session['cart'][product_id]
            print(' minus current_quantity:', current_quantity)
            new_quantity = current_quantity-1

            if new_quantity <= 0:
                new_quantity = 1
                self.session['cart'][product_id] = new_quantity
                self.session.save()
                print('minus <= 0:: после изменений', self.session['cart'])
            else:
                self.session['cart'][product_id] = new_quantity
                self.session.save()
                print('minus после изменений', self.session['cart'])

    def remove(self,product_id):

        print('remove до удаления', self.session['cart'])
        if product_id in self.session['cart']:
            del self.session['cart'][product_id]
            self.session['cart'] = self.session['cart'].copy()
            print('remove после удаления', self.session['cart'])
