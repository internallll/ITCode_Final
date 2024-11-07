from django.test import TestCase

from detailShop.factories import OrderFactory, DetailFactory, OrderElementFactory
from detailShop.models import Order, Detail, OrderElement


class detailShopTestCase(TestCase):

  def test_create_order(self):
    order = OrderFactory()

    self.assertIsInstance(order, Order)
    self.assertIsNotNone(order.pk)
    self.assertIsNotNone(order.customer)
    self.assertIn(order.status, ["Отменен", "В обработке", "Доставлен"])

  def test_create_detail(self):
    detail = DetailFactory()

    self.assertIsInstance(detail, Detail)
    self.assertIsNotNone(detail.pk)
    self.assertTrue(detail.name)
    self.assertGreater(detail.price, 0)

  def test_create_order_element(self):
    order_element = OrderElementFactory()

    self.assertIsInstance(order_element, OrderElement)
    self.assertIsNotNone(order_element.pk)
    self.assertIsNotNone(order_element.detail)
    self.assertGreater(order_element.count, 0)
