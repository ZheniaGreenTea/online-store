from django.contrib import admin
from .models import Category,Ganre,Translator,Writer,PublishingHouse,Product,ProductImage

admin.site.register(Category)
admin.site.register(Ganre)
admin.site.register(Translator)
admin.site.register(Writer)
admin.site.register(PublishingHouse)
admin.site.register(Product)
admin.site.register(ProductImage)
