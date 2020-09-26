from django.db import models
from django.contrib.auth.models import User


class OrderProduct(models.Model):
    """модель копии продукта"""
    name = models.CharField('название товара', max_length=250)
    author = models.CharField('автор в заказе', max_length=250)
    description = models.TextField('описание')
    price = models.FloatField('цена')
    product_id = models.BigIntegerField('id продукта',)


    def __str__(self):
        return '{0} {1} {2} '.format(self.name, self.author, self.price)

    class Meta:
        verbose_name = "Копия заказа"
        verbose_name_plural = "Копия заказов"

class DepartmentDelivery(models.Model):
    """модель самовывоза"""
    address = models.CharField('адресса самовывоза', max_length=250)
    is_active = models.BooleanField('отображать?', default=True)


    def __str__(self):
        return '{0} {1}  '.format(self.address,  self.is_active,)

    class Meta:
        verbose_name = "Самовывоз"
        verbose_name_plural = "Самовывоз"



class DeliveryMan(models.Model):
    """модель доставка курьером"""
    address = models.CharField('адресс доставки', max_length=250)
    home_number = models.CharField('номер дома', max_length=250)
    flat_number = models.CharField('номер квартиры', max_length=250,blank=True, null=True)
    door_number = models.PositiveIntegerField('подъезд',blank=True, null=True)

    def __str__(self):
        return '{0} {1} {2} {3} '.format(self.address, self.home_number, self.flat_number, self.door_number )


    class Meta:
        verbose_name = "Курьерская доставка"
        verbose_name_plural = "Курьерская доставка"





class NovayaPochta(models.Model):
    """модель адресса почтового отделения Новой Почты"""

    address = models.CharField('отделение Новой Почты', max_length=250)

    def __str__(self):
        return '{0}  '.format( self.address)

    class Meta:
        verbose_name = "Отделение Новой Почты"
        verbose_name_plural = "Отделения Новой Почты"


class UkrPochta(models.Model):
    """модель адресса почтового отделения Укр Почты"""

    address = models.CharField('отделение Укр Почты', max_length=250)

    def __str__(self):
        return '{0} {1} '.format( self.address,self.id)

    class Meta:
        verbose_name = "Отделение Укр Почты"
        verbose_name_plural = "Отделения Укр Почты"




class Status(models.Model):
    """модель статуса выполнения заказа"""
    name = models.CharField("cтатус заказа", max_length=50, blank=True, null=True)
    create = models.DateTimeField('дата cоздания статуса ', auto_now_add=True)
    update = models.DateTimeField('дата изменения статуса ', auto_now=True)

    def __str__(self):
        return '{0}   '.format(self.name)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"





class Order(models.Model):
    """модель  заказа"""
    user = models.ForeignKey(User, related_name='userorders', verbose_name="Покупатель", on_delete=models.CASCADE,
                             blank=True, null=True)
    name = models.CharField('имя заказчика', max_length=250,null=True)
    last_name = models.CharField('фамилия заказчика', max_length=250,null=True)
    telephone = models.CharField('телефон заказчика', max_length=250,null=True)
    email = models.CharField('эл. заказчика', max_length=250,null=True)
    user_comment = models.TextField("комментарий заказчика",blank=True,
                                            null=True)
    admin_comment = models.TextField("комментарий администратора",blank=True,
                                            null=True)
    order_product = models.ForeignKey(OrderProduct, verbose_name="копия заказ", on_delete=models.CASCADE,blank=True, null=True)
    current_status = models.ForeignKey(Status, verbose_name="статус заказа", on_delete=models.CASCADE, default=1, blank=True)
    responsible_manager = models.ForeignKey(User, verbose_name="ответственный менеджер", related_name='managerorders', on_delete=models.CASCADE, blank=True,
                                            null=True)
    responsible_delivery_man = models.ForeignKey(User, verbose_name="ответственный за доставку", related_name='deliveryorders', on_delete=models.CASCADE,
                                                 blank=True, null=True)
    city_delivery = models.CharField('город', max_length=250,null=True)
    departmen_way = models.ForeignKey(DepartmentDelivery, verbose_name="самовывоз",on_delete=models.CASCADE, blank=True, null=True)
    deliveryman_way = models.ForeignKey(DeliveryMan, verbose_name="курьерская доставка", on_delete=models.CASCADE, blank=True, null=True)
    nova_post_office = models.ForeignKey(NovayaPochta, verbose_name="доставка новой почтой",on_delete=models.CASCADE, blank=True, null=True)
    ukr_post_office = models.ForeignKey(UkrPochta, verbose_name="доставка новой почтой", on_delete=models.CASCADE,
                                         blank=True, null=True)
    payment_method = models.CharField('способ оплаты', max_length=250,blank=True,null=True)

    def __str__(self):
        return '{0} {1} {2} {3} {4} {5} {6} {7} {8}'.format(self.user, self.user_comment, self.admin_comment, self.order_product,
                                            self.current_status, self.departmen_way, self.deliveryman_way, self.nova_post_office,self.ukr_post_office )

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"








