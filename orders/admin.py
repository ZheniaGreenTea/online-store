from django.contrib import admin
from .models import Order,OrderProduct,Status,DepartmentDelivery,DeliveryMan,NovayaPochta,UkrPochta

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)



admin.site.register(Status, StatusAdmin)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(DepartmentDelivery)
admin.site.register(DeliveryMan)
admin.site.register(NovayaPochta)
admin.site.register(UkrPochta)

