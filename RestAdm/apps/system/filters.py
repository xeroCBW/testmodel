import django_filters

from system.models import Good,Button


class GoodFilter(django_filters.rest_framework.FilterSet):


    class Meta:
        model = Good
        fields = ['is_new','is_hot',]

class ButtonFilter(django_filters.rest_framework.FilterSet):

    class Meta:

        model = Button
        fields = ['id',]
