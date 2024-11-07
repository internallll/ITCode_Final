import factory
from factory.django import ImageField

from detailShop import models
from detailShop.models import Detail, OrderElement


class OrderFactory(factory.django.DjangoModelFactory):
    customer = factory.Faker('text')
    address_delivery = factory.Faker('address')
    comment = factory.Faker('text', max_nb_chars=200)
    phone_number = factory.Faker('phone_number')
    status = factory.Faker('random_element', elements=["Отменен", "В обработке", "Доставлен"])
    sum = factory.Faker('random_int', min=0, max=1200)
    class Meta:
        model = models.Order

class DetailFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('sentence')
    description = factory.Faker('text')
    price = factory.Faker('random_int', min=0, max=12000)
    country_prod = factory.Faker('country')
    image = ImageField()

    class Meta:
        model = Detail


class OrderElementFactory(factory.django.DjangoModelFactory):
    detail = factory.SubFactory(DetailFactory)
    order = factory.SubFactory(OrderFactory)
    count = factory.Faker('random_int', min=1, max=10)

    class Meta:
        model = OrderElement