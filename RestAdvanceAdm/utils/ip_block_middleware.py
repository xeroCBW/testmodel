from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework import status


class IPBlockMiddleWare(MiddlewareMixin):

    def process_request(self, request):

        EXCLUDE_IPS = [

            '0.0.0.0',
            '127.0.0.1'
        ]
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        if ip in EXCLUDE_IPS:
            print('------')
            return JsonResponse(data={'msg': '访问过多,稍后再试', 'data': {}, 'code': 401},
                                status=status.HTTP_401_UNAUTHORIZED)

