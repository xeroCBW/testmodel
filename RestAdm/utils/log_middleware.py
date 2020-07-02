import json
import socket
import time
import logging

from django.http import QueryDict
from django.utils.deprecation import MiddlewareMixin

class RequestLogMiddleware(MiddlewareMixin):

    def __init__(self, get_response=None):
        self.get_response = get_response
        self.apiLogger = logging.getLogger('api')
        # super().__init__()

    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):

        # print('----RequestLogMiddleware start ....---')
        request_body = dict()

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

        response_body = dict()
        if response.accepted_media_type and response.accepted_media_type == 'application/json':
            response_body = response.data
        else:
            response_body = "<<<NOT JSON>>>"

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

        # print(json.dumps(log_data,indent=4,ensure_ascii=False))

        # try:
        #     body = json.loads(request.body)
        # except Exception:
        #     body = dict()
        # body.update(dict(request.POST))

        self.apiLogger.info("{} {} {} {} {} {}".format(
            request.user, request.method, request.path,json.dumps(log_data,ensure_ascii=False),
            response.status_code, response.reason_phrase))

        return response