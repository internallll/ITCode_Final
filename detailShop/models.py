from django.db import models
from django.template.defaultfilters import length


class Detail(models.Model):
    name = models.CharField(verbose_name='Название детали', max_length=255)
    description = models.TextField(verbose_name='Описание детали', blank=True)
    price = models.IntegerField(verbose_name='Цена детали', blank=True)
    country_prod =models.CharField(verbose_name='Страна производства', max_length=255, blank=True)
    image = models.ImageField(upload_to='media', null = True, blank = True)

    storage = models.ForeignKey(
        'Storage',
        on_delete=models.CASCADE, null=True, blank=True

    )

    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE, related_name='category_detail', null = True
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
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона", null = True)
    status = models.CharField(max_length=50, default='В обработке', verbose_name="Статус заказа")
    sum = models.IntegerField(default=0, verbose_name='Сумма заказа')


    def calculate_sum(self):
        total_sum = 0
        for element in self.order_elements.all():
            total_sum += element.detail.price * element.count  # Умножаем цену детали на количество
        self.sum = total_sum
        self.save()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering =['-customer']



    def __str__(self):
        return f"Заказ № {self.pk} | Покупатель {self.customer}"



class OrderElement(models.Model):
    detail = models.ForeignKey('Detail',
                               on_delete=models.CASCADE, verbose_name="Деталь")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_elements', verbose_name="Заказ", blank=True, null=True)
    count = models.IntegerField(verbose_name='Количество элементов',blank=True, default=1)

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'
        ordering = ['-detail']

    def __str__(self):
       return f'Товар {self.detail} | Заказ № {self.order.pk}'

class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=255)

    class Meta:
        verbose_name = 'Категория детали'
        verbose_name_plural = 'Категории детали'
        ordering = ['-name']

    def __str__(self):
        return self.name