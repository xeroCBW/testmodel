import django_filters

from system.models import *


class UserFilter(django_filters.rest_framework.FilterSet):
    '''
    商品过滤的类
    '''
    #两个参数，name是要过滤的字段，lookup是执行的行为，‘小与等于本店价格’
    id_min = django_filters.NumberFilter(name="id", lookup_expr='gte')
    id_max = django_filters.NumberFilter(name="id", lookup_expr='lte')

    class Meta:
        model = UserProfile
        fields = ['id_min', 'id_max']