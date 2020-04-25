from django.forms import ModelForm
from .models import Product


class ProductAdd(ModelForm):
        
        class Meta:
            model = Product
            fields = ('quantity', )
            labels = {
            "quantity": ""}
