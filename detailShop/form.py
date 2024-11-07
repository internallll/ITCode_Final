from django.forms import  modelformset_factory
from django import forms
from detailShop.models import OrderElement, Order


class OrderElementForm(forms.ModelForm):
    class Meta:
        model = OrderElement
        fields = ['detail', 'count']

OrderElementFormSet = modelformset_factory(OrderElement, form=OrderElementForm, extra=1)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'address_delivery', 'comment', 'phone_number']