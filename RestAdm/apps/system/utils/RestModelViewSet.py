from rest_framework import status
from rest_framework import viewsets
from .RestResponse import JsonResponse
from rest_framework import filters
from django_filters import rest_framework
from rest_framework import mixins


class CustomBaseModelViewSet(viewsets.ModelViewSet):
    # pagination_class = LargeResultsSetPagination
    # filter_class = ServerFilter
    # queryset = ''
    # serializer_class = ''
    # permission_classes = ()
    # filter_fields = ()
    # search_fields = ()
    # filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return JsonResponse(data=serializer.data, msg="success", code=201,
                            status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # 增加item属性
        serializer = self.get_serializer(queryset, many=True)
        res = {'items':serializer.data}
        return JsonResponse(data=res, code=200, msg="success", status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return JsonResponse(data=serializer.data, code=200, msg="success", status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return JsonResponse(data=serializer.data, msg="success", code=200, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return JsonResponse(data=[], code=204, msg="delete resource success", status=status.HTTP_204_NO_CONTENT)



class CustomBaseCreateModelMixin(mixins.CreateModelMixin):
    def create(self, request, *args, **kwargs):
        return CustomBaseModelViewSet.create(request,*args,**kwargs)


class CustomBaseRetrieveModelMixin(mixins.RetrieveModelMixin):
    def retrieve(self, request, *args, **kwargs):
        return CustomBaseModelViewSet.retrieve(request,*args,**kwargs)


class CustomBaseUpdateModelMixin(mixins.UpdateModelMixin):
    def update(self, request, *args, **kwargs):
        return CustomBaseModelViewSet.update(request,*args,**kwargs)


class CustomBaseDestroyModelMixin(mixins.DestroyModelMixin):
    def destroy(self, request, *args, **kwargs):
        return CustomBaseModelViewSet.retrieve(request,*args,**kwargs)


class CustomBaseListModelMixin(mixins.ListModelMixin):
    def list(self, request, *args, **kwargs):
        return CustomBaseModelViewSet.list(request,*args,**kwargs)