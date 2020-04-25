from django.contrib import admin
from .models import Order,OrderProduct,Status
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Status)
# Register your models here.
