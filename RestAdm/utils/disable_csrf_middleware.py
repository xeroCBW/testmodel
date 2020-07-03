from django.utils.deprecation import MiddlewareMixin


class DisableCSRFCheck(MiddlewareMixin):
    def process_request(self, request):
        # print('-------')
        setattr(request, '_dont_enforce_csrf_checks', True)