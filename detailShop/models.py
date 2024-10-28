from django.db import models


class Car(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    generation = models.ForeignKey(
        'Generation',
        on_delete=models.CASCADE, related_name='generation_car', null=True

    )
    class Meta:
        verbose_name='Машина'
        verbose_name_plural = 'Машины'
        ordering =['-name']

    def __str__(self):
        return self.name


class Generation(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    year_start = models.IntegerField(verbose_name='Год начала выпуска', blank=True)
    year_end = models.IntegerField(verbose_name='', blank=True)
    image = models.ImageField(upload_to='media', null = True, blank = True)

    class Meta:
        verbose_name = 'Поколение'
        verbose_name_plural = 'Поколения'
        ordering = ['-title']

    def __str__(self):
        return self.title

class Detail(models.Model):
    name = models.CharField(verbose_name='Название детали', max_length=255)
    description = models.TextField(verbose_name='Описание детали', blank=True)
    price = models.IntegerField(verbose_name='Цена детали', blank=True)
    country_prod =models.CharField(verbose_name='Страна производства', max_length=255, blank=True)
    storage = models.ForeignKey(
        'Storage',
        on_delete=models.CASCADE

    )
    car = models.ForeignKey(
        'Car',
        on_delete=models.CASCADE, default=1,
        related_name ='car_detail'
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'
        ordering = ['-name']

class Storage(models.Model):
    name = models.CharField(verbose_name='Название склада',max_length=255, null = True)
    address =models.CharField(verbose_name='Адрес склада',max_length=255, blank =True, null = True)
    capacity = models.IntegerField(verbose_name='Вместимость', blank=True, null=True)

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(verbose_name='Имя поставщика', max_length=255)
    phone_number = models.IntegerField(verbose_name='Номер телефона поставщика', blank=True)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering =['-name']


    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.CharField(verbose_name='Заказчик', max_length=255)
    address_delivery = models.CharField(verbose_name='Адрес доставки', max_length=255,blank=True)
    comment = models.TextField(verbose_name='Комментарий к заказу', blank=True)



    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering =['-customer']



    def __str__(self):
        return self.customer



class OrderElement(models.Model):
    detail = models.ForeignKey('Detail',
                               on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_elements', blank=True, null=True)
    count = models.IntegerField(verbose_name='Количество элементов',blank=True, default=1)

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'
        ordering = ['-detail']

    def __str__(self):
       return f'{self.count} x {self.detail.name}'