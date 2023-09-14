from .models import Lender
import django_filters


class ActiveLenderFilter(django_filters.FilterSet):
    active = django_filters.BooleanFilter()

    class Meta:
        model = Lender
        fields = ('active',)


class SearchLenderFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Name', max_length=255, lookup_expr='icontains')
    code = django_filters.CharFilter(label='Code', max_length=3, lookup_expr='icontains')
    upfront_com = django_filters.NumberFilter()
    trial_com = django_filters.NumberFilter()
    active = django_filters.BooleanFilter()

    class Meta:
        model = Lender
        fields = ('name', 'code', 'upfront_com', 'trial_com', 'active')
