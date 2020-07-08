import django_filters
from system.models import Good, Button, Role, Page, UserProfile


class GoodFilter(django_filters.rest_framework.FilterSet):


    class Meta:
        model = Good
        fields = ['is_new','is_hot',]

class RoleFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Role
        fields = ['id',]

class PageFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Page
        fields = ['id',]

class ButtonFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Button
        fields = ['id',]


class UserFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = UserProfile
        fields = ['id',]