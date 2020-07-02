from uuid import uuid4
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from jwt import InvalidSignatureError
from rest_framework.exceptions import ValidationError
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework import status
import json
from django.http import QueryDict

class CheckTokenMiddleware(MiddlewareMixin):
    '''
    Django 1.4.x ---- Django 1.9.x
    每次请求时 判断 JWT 是否与 User.user_jwt 相等
    相等的话，说明没有以设备登录，且没有修改密码
    不相等，则说明异常设备登录，或修改了密码，修改用户的uuid并提示用户重新登录
    每次登录时记录更新JWT 为User 的一个属性user_jwt
    每次修改密码时 更新修改uuid
    '''

    def process_request(self,request):

        print('----CheckTokenMiddleware request start ....---')
        print(request.path)
        if request.method == 'POST':
            print(json.dumps(request.POST,ensure_ascii=False,indent=4))

        if request.method == 'PUT':
            print(json.dumps(QueryDict(request.body), ensure_ascii=False, indent=4))


        jwt_token = request.META.get('Authorization', None)
        if jwt_token is not None and jwt_token != '':
            data = {
                'token': jwt_token.split(' ')[1],  # [0] 是前缀，默认为JWT
            }

            try:
                valid_data = VerifyJSONWebTokenSerializer().validate(data)
                user = valid_data['user']
            except (InvalidSignatureError, ValidationError):
                # 找不到用户，说明token 不合法或者身份过期
                return HttpResponse({'msg': '身份已经过期，请重新登入'}, content_type='application/json', status=status.HTTP_401_UNAUTHORIZED)
            if user.user_jwt != data['token']:
                user.user_secret = uuid4()
                user.save()
                return HttpResponse("{'msg','请重新登入'}", content_type='application/json', status=status.HTTP_401_UNAUTHORIZED)

    def process_response(self, request, response):
        # 仅用于处理 login请求
        if request.META['PATH_INFO'] == '/user/login/':
            rep_data = response.data
            valid_data = VerifyJSONWebTokenSerializer().validate(rep_data)
            user = valid_data['user']
            user.user_jwt = rep_data['token']
            user.save()
            return response
        else:
            print('----CheckTokenMiddleware resonse start ....---')
            print(json.dumps(response.data, ensure_ascii=False, indent=4))
            return response

