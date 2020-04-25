from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):

    name = models.CharField("cтатус заказа", max_length=50, blank=True, null=True)
    create = models.DateTimeField('дата cоздания статуса ', auto_now_add=True)
    update = models.DateTimeField('дата изменения статуса ', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"



class OrderProduct(models.Model):


        name = models.CharField('название товара', max_length=250)
        author = models.CharField('автор в заказе', max_length=250)
        description = models.TextField(blank=True)
        price = models.FloatField()

        def __str__(self):
            return self.name

        class Meta:
            verbose_name = "Копия заказа"
            verbose_name_plural = "Копия заказов"




class Order(models.Model):

    user = models.ForeignKey(User,related_name='userorders',verbose_name="Покупатель", on_delete=models.CASCADE)
    user_comment = models.TextField("комментарий юзера")
    admin_comment = models.TextField("комментарий администратора")
    order_product = models.ForeignKey(OrderProduct,verbose_name="копия заказ в корзину", on_delete=models.CASCADE)
    current_status = models.ForeignKey(Status,verbose_name="статус заказа", on_delete=models.CASCADE)
    responsible_manager = models.ForeignKey(User,related_name='managerorders', on_delete=models.CASCADE,  blank=True, null=True)
    responsible_delivery_man = models.ForeignKey(User,related_name='deliveryorders', on_delete=models.CASCADE)


    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"



class Delivery(models.Model):
    """модель самовывоза товара"""

    address = models.CharField('адресса самовывоза', max_length=250)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    is_active = models.BooleanField('отображать?', default=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Доставка"
        verbose_name_plural = "Доставка"






