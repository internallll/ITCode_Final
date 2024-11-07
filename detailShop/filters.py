import django_filters

from detailShop.models import Detail


class DetailFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label ='Название')
    country_prod = django_filters.CharFilter( lookup_expr='icontains', label='Страна производства')

    class Meta:
        model = Detail
        fields = ['name','country_prod']