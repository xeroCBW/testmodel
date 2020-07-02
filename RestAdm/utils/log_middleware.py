import json
import socket
import time

from django.http import QueryDict
from django.utils.deprecation import MiddlewareMixin

class RequestLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):

        print('----RequestLogMiddleware start ....---')
        request_body = {}
        if request.method == 'POST':
            request_body = request.POST
        if request.method == 'PUT':
            request_body = QueryDict(request.body)

        # if response['content-type'] == 'application/json':
        #     if getattr(response, 'streaming', False):
        #         response_body = '<<<Streaming>>>'
        #     else:
        #         response_body = response.content
        # else:
        #     response_body = '<<<Not JSON>>>'

        response_body = response.data

        log_data = {
            'user': request.user.pk,

            'remote_address': request.META['REMOTE_ADDR'],
            'server_hostname': socket.gethostname(),

            'request_method': request.method,
            'request_path': request.get_full_path(),
            'request_body': request_body,

            'response_status': response.status_code,
            'response_body': response_body,

            'run_time': time.time() - request.start_time,
        }

        print(json.dumps(log_data,indent=4,ensure_ascii=False))
        # save log_data in some way
        return response