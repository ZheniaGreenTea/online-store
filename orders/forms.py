from django.forms import ModelForm, forms

from .models import Order, NovayaPochta


class OrderForm(ModelForm):

    class Meta:
        model = Order

        fields = ('name','last_name','telephone','email','user_comment','admin_comment','admin_comment',
                  'order_product','current_status','city_delivery','departmen_way','nova_post_office','ukr_post_office','deliveryman_way',)

