from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator



class Ganre(models.Model):

    name = models.CharField('жанр книги',max_length=250)

    class Meta:

        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
            return self.name




class Translator(models.Model):

    first_name = models.CharField('имя переводчика',max_length=250)
    last_name = models.CharField('фамилия переводчика',max_length=250)

    class Meta:

        verbose_name = "Переводчик"
        verbose_name_plural = "Переводчики"

    def __str__(self):
        return '{0} {1} '.format(self.first_name, self.last_name)



class Writer(models.Model):

    first_name = models.CharField('имя автора',max_length=250)
    last_name = models.CharField('фамилия автора',max_length=250)

    class Meta:

        verbose_name = "Писатель"
        verbose_name_plural = "Писатели"

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class PublishingHouse(models.Model):

    name = models.CharField('издательство', max_length=250)

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'

    def __str__(self):
        return self.name



class Category(models.Model):

    name = models.CharField('категория',max_length=250)
    slug = models.SlugField('url',max_length=250,unique=True)

    class Meta:

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name



def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)




class Product(models.Model):

    name = models.CharField('название товара', max_length=250)
    author = models.ManyToManyField(Writer, verbose_name="автор")
    quantity = models.PositiveIntegerField(default=0)
    pub_house = models.ForeignKey(PublishingHouse,verbose_name="издательство",on_delete=models.CASCADE)
    age_choice = (('для детей','для детей'),
                                ('для школьников','для школьников'),
                                ('для подростков','для подростков'),
                                ('для взрослых','для взрослых'),
                                ('для всех возрастов','для всех возрастов'),
                                ('0+', '0+'),
                                ('16+', '16+'),
                                ('18+', '18+'),
                                ('12+','12+'))
    age = models.CharField("возрастное ограничение",max_length=250,blank=True, null=True, choices=age_choice)
    pub_year = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1900), max_value_current_year])
    language_choice = (('укранский','укранский'),('английский','английский'),('русский','русский'))
    language = models.CharField("язык",max_length=250,blank=True, null=True, choices=language_choice)
    translator = models.ManyToManyField(Translator, verbose_name="переводчик",blank=True)
    ganre = models.ManyToManyField(Ganre, verbose_name="жанр")
    slug = models.SlugField('url',max_length=200,unique=True)
    description = models.TextField('описание', blank=True)
    total_pages = models.PositiveIntegerField('количество страниц',blank=True, null=True)
    price = models.FloatField("цена", default=0)
    stock = models.FloatField("скидки",default=0)
    to_show = models.BooleanField('отображать?',default=True)
    create_date = models.DateTimeField('дата загрузки ', auto_now_add=True)
    up_date = models.DateTimeField('дата обновления ', auto_now=True)
    category = models.ForeignKey(Category, verbose_name="категория",on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name



class ProductImage(models.Model):
    images = models.ForeignKey(Product, verbose_name="фото товара", blank=True, null=True,
                               on_delete=models.CASCADE)
    path = models.ImageField(upload_to='products_images/')
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField('дата создания ', auto_now_add=True)
    up_date = models.DateTimeField('дата обновления ', auto_now=True)


    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

